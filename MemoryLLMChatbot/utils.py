from .models import Message

def get_message_history(user):
    SYSTEM_PROMPT = "You are a helpful AI assistant with a friendly, anime-inspired personality. Answer questions concisely and accurately, adding a touch of fun!"
    all_messages = Message.objects.filter(user=user).order_by('timestamp')
    message_history = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in all_messages:
        message_history.append({"role": msg.role, "content": msg.content})
    return message_history