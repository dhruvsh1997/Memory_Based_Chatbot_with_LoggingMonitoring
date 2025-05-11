from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Message
from groq import Groq
from django.conf import settings
from django.http import JsonResponse
import json
import logging

# Initialize Groq client
client_groq = Groq(api_key=settings.GROQ_API_KEY)

# Set up logging
logger = logging.getLogger('MemoryLLMChatbot')

SYSTEM_PROMPT = "You are a helpful AI assistant with a friendly, anime-inspired personality. Answer questions concisely and accurately, adding a touch of fun!"

@login_required
def chat(request):
    messages = Message.objects.filter(user=request.user).order_by('timestamp')
    logger.info(f"User {request.user.username} accessed chat interface")
    return render(request, 'MemoryLLMChatbot/chat.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')
        if user_message:
            # Save user's message
            Message.objects.create(user=request.user, role='user', content=user_message)
            logger.debug(f"User {request.user.username} sent message: {user_message}")
            
            # Get all messages for the user
            all_messages = Message.objects.filter(user=request.user).order_by('timestamp')
            
            # Prepare message_history for Groq
            message_history = [{"role": "system", "content": SYSTEM_PROMPT}]
            for msg in all_messages:
                message_history.append({"role": msg.role, "content": msg.content})
            
            # Call Groq API
            try:
                response = client_groq.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=message_history
                )
                assistant_response = response.choices[0].message.content
                # Save assistant's response
                Message.objects.create(user=request.user, role='assistant', content=assistant_response)
                logger.debug(f"Assistant responded with: {assistant_response}")
                return JsonResponse({'message': assistant_response})
            except Exception as e:
                logger.error(f"Error generating response: {str(e)}")
                return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f"New user registered: {user.username}")
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'MemoryLLMChatbot/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User logged in: {user.username}")
            return redirect('chat')
    else:
        form = AuthenticationForm()
    return render(request, 'MemoryLLMChatbot/login.html', {'form': form})

def logout_view(request):
    logger.info(f"User logged out: {request.user.username}")
    logout(request)
    return redirect('login')