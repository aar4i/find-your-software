FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY flaskr/ ./flaskr/

# Expose Flask port
EXPOSE 5000

# Run Flask
ENV FLASK_APP=flaskr
CMD ["flask", "run", "--host=0.0.0.0"]