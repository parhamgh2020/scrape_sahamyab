# Use the official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -yq curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -yq nodejs && \
    npm install -g playwright

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN pip install virtualenv && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN playwright install
RUN playwright install-deps

# Run the command to start the app
CMD ["python", "main.py"]
