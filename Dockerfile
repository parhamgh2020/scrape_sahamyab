# Use the official Python runtime as a parent image
FROM ubuntu:22.04
# Set the working directory to /app
WORKDIR /app

RUN apt-get update
RUN apt -y upgrade
RUN apt -y install python3-pip
RUN apt-get -y install libnss3 libatk-bridge2.0-0 libdrm-dev libxkbcommon-dev libgbm-dev libasound-dev libatspi2.0-0 libxshmfence-dev

RUN apt -y install build-essential libssl-dev libffi-dev python3-dev

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install playwright

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
