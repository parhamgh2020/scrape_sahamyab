FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

# Add python script to Docker
COPY . .

RUN apt-get update && apt-get -y upgrade
RUN pip install -r requirements.txt

# Run Python script
CMD [ "python", "main.py" ]
