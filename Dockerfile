FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

# Add python script to Docker
COPY . .

RUN pip install -r requirements.txt

# Run Python script
CMD [ "python", "main.py" ]







## FROM mcr.microsoft.com/playwright/python:v1.30.0-focal
#FROM ubuntu:22.04
## Install any necessary packages
#RUN apt-get update && apt-get install -y python3 python3-pip
#RUN pip install --upgrade pip
#
## Set the working directory to /app
#WORKDIR /app
#RUN pip install virtualenv
#
## Copy the requirements file into the container
#COPY . .
#
## Install the dependencies
#RUN python3 -m virtualenv venv && \
#    . venv/bin/activate && \
#    pip install --no-cache-dir -r requirements.txt && \
#    playwright install chromium && \
#    python3 main.py
#
## # Start the app
## CMD [ "python3", "app.py" ]
