# MemoryLLMChatLog: Anime-Inspired AI Chatbot with Memory 🌸✨

Welcome to **MemoryLLMChatLog**, a Django-powered chatbot that bring the magic of anime to your conversations! Powered by the **Groq API**, this project features a delightful, cartoonish UI, user session management, and conversation memory to keep your chats seamless and fun. With robust logging and monitoring, it’s perfect for developers looking to explore AI chatbot development with a touch of kawaii charm! 😺

![Anime Chatbot Banner](https://via.placeholder.com/800x200.png?text=Anime+MemoryLLMChatbot) <!-- Replace with actual banner -->

---

## 🚀 Features

- **Anime-Inspired UI**: Bright colors, rounded corners, and a playful font create a vibrant, cartoonish interface. 🌈
- **Groq API Integration**: Leverages the `llama-3.3-70b-versatile` model for smart, concise responses. 🧠
- **Conversation Memory**: Stores chat history per user in a SQLite database, ensuring personalized interactions. 📜
- **User Authentication**: Secure login, registration, and logout with Django’s authentication system. 🔐
- **AJAX-Powered Chat**: Real-time message sending and receiving with jQuery for a smooth experience. ⚡
- **Logging & Monitoring**: Comprehensive logging with Django’s `logging` module to track user actions and errors. 📊
- **Docker Support**: Containerized setup with secure Groq API key management for easy deployment. 🐳
- **Responsive Design**: Built with Bootstrap for a mobile-friendly interface. 📱

---

## 🛠️ Project Structure

```
MemoryLLMChatLog/
├── manage.py
├── MemoryLLMChatLog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── MemoryLLMChatbot/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── static/
│   │   └── MemoryLLMChatbot/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── MemoryLLMChatbot/
│   │       ├── base.html
│   │       ├── chat.html
│   │       ├── login.html
│   │       ├── register.html
├── requirements.txt
├── Dockerfile
├── README.md
```

---

## 📋 Prerequisites

- **Python 3.11** 🐍
- **Docker** (optional, for containerized setup) 🐳
- **Groq API Key** (sign up at [Groq Console](https://console.groq.com/) to get one) 🔑
- A passion for anime and AI! 😻

---

## ⚙️ Setup Instructions

Follow these steps to get your chatbot up and running locally!

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MemoryLLMChatLog.git
cd MemoryLLMChatLog
```

### 2. Install Dependencies
Create a virtual environment and install the required packages:
```bash
python -m venv .envMemChatLog
source .envMemChatLog/bin/activate  # On Windows: .envMemChatLog\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Groq API Key
Set your Groq API key as an environment variable:
```bash
export GROQ_API_KEY='your-groq-api-key'  # On Windows: set GROQ_API_KEY=your-groq-api-key
```
Alternatively, create a `.env` file in the project root:
```text
GROQ_API_KEY=your-groq-api-key
```
Ensure `python-dotenv` is installed (`pip install python-dotenv`) and update `settings.py` to load it:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Apply Migrations
Set up the SQLite database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Collect Static Files
Gather static files for the anime-inspired UI:
```bash
python manage.py collectstatic
```

### 6. Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

### 7. Access the Chatbot
Open your browser and navigate to:
- **Login**: `http://127.0.0.1:8000/`
- **Register**: `http://127.0.0.1:8000/register/`
- **Chat**: `http://127.0.0.1:8000/chat/` (after logging in)

---

## 🐳 Running with Docker

For a containerized setup with secure Groq API key management:

### 1. Build the Docker Image
```bash
docker build -t memoryllmchatlog .
```

### 2. Run the Container
Pass the Groq API key as an environment variable:
```bash
docker run -e GROQ_API_KEY=your-groq-api-key -p 8000:8000 memoryllmchatlog
```

Alternatively, use Docker Compose for easier management:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - GROQ_API_KEY=your-groq-api-key
    volumes:
      - .:/app
```
Run with:
```bash
docker-compose up
```

### 3. Access the Chatbot
Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Groq API Key Management

To keep your Groq API key secure:
- **Development**: Use environment variables (`export GROQ_API_KEY=...`) or a `.env` file.
- **Production**: Use a secrets manager (e.g., AWS Secrets Manager) or Docker secrets.
- **Never** commit the API key to version control. Add `.env` to `.gitignore`:
  ```text
  .env
  *.log
  staticfiles/
  db.sqlite3
  ```

---

## 📊 Logging & Monitoring

The chatbot includes robust logging to monitor user interactions and errors:
- **Logger**: `MemoryLLMChatbot` captures events in the app.
- **Handler**: Writes logs to `chatbot.log` in the project root.
- **Formatter**: Uses a verbose format (`{levelname} {asctime} {module} {message}`).
- **Filter**: Logs only when `DEBUG=True` (configurable in `settings.py`).

View logs in `chatbot.log`:
```text
DEBUG 2025-05-11 16:02:34,123 views User dhruv sent message: Hello
INFO 2025-05-11 16:02:34,125 views User dhruv accessed chat interface
```

---

## 🎨 Anime-Inspired UI

The chatbot’s UI is designed to feel like an anime adventure:
- **Colors**: Hot pink (`#ff69b4`) and dodger blue (`#1e90ff`) for a vibrant look.
- **Font**: `Anime Ace` (or `Comic Sans MS` fallback) for a playful vibe.
- **Design**: Rounded corners, shadows, and a responsive Bootstrap layout.
- **Enhancements**: Add animations with [Animate.css](https://animate.style/) or anime avatars for extra flair!

---

## 🛠️ Troubleshooting

- **TemplateDoesNotExist**: Ensure templates are in `MemoryLLMChatbot/templates/MemoryLLMChatbot/`.
- **jQuery Error (`$ is not defined`)**: Verify jQuery loads in `base.html` (check browser console).
- **Groq API Errors**: Confirm `GROQ_API_KEY` is set correctly.
- **Static Files**: Run `python manage.py collectstatic` and check `STATICFILES_DIRS` in `settings.py`.
- **Logs**: Check `chatbot.log` for detailed error messages.

For further help, open an issue or contact the maintainers! 😺

---

## 🤝 Contributing

We’d love for you to join our anime chatbot adventure! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and add tests for new features.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- **Groq API** for powering our AI responses.
- **Django** for a robust web framework.
- **Bootstrap** for responsive design.
- **Anime Aesthetic** inspired by the vibrant world of anime! 🌸

---

**Ready to chat with your anime-inspired AI companion? Let’s dive into the adventure!** 😻
