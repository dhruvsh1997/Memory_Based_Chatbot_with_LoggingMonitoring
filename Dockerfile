# Use a slim Python 3.11 base image for a smaller footprint
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Set environment variables
# Prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (if needed, e.g., for SQLite or other tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Collect static files (assumes STATIC_ROOT is set in settings.py)
RUN python manage.py collectstatic --noinput

# Run migrations during container startup
RUN python manage.py migrate

# Expose port 8000 for the Django server
EXPOSE 8000

# Command to run the Django development server
# Note: For production, consider using gunicorn (uncomment below)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "MemoryLLMChatLog.wsgi:application"]