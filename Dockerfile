# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Set a working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your code
COPY . /app/

# Expose the port (Cloud Run expects 8080 by default)
ENV PORT=8080
EXPOSE 8080

# Start server (gunicorn, for example)
CMD ["gunicorn", "--bind", ":8080", "portfolio.wsgi:application"]
