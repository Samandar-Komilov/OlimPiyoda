# Base image with Python 3.10 Alpine
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements/ ./requirements
RUN pip install --no-cache-dir -r requirements/base.txt

# Copy project files into the container
COPY . /app/

# Set executable permission
RUN chmod +x /app/entrypoint.dev.sh

# Expose port for Django server
EXPOSE 8000
