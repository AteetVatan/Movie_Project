# Use slim Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (for psycopg2 or similar)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

ENV FLASK_ENV=production

EXPOSE 5001

CMD ["python", "main.py"]

#docker build -t movie-app .
#docker run -p 5001:5001 --env-file config/.env movie-app
#Now your Flask MVC app is live at 👉 http://localhost:5001