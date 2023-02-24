# Use the official Python runtime as a parent image
FROM ubuntu:22.04
# Set the working directory to /app
WORKDIR /app

RUN apt-get update && apt-get upgrade && \
    apt install python3 && \
    apt install -y python3-pip

#RUN apt install -y build-essential libssl-dev libffi-dev python3-dev

# Install dependencies
#RUN apt-get update && apt-get install -yq curl && \
#    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
#    apt-get install -yq nodejs && \
#    npm install -g playwright

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN pip install virtualenv && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install chromium && \
    python3 main.py


# Run the command to start the app
#CMD ["python", "main.py"]
