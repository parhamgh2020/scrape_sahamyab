FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

RUN apt-get update && apt-get -y upgrade
RUN apt install python3-pip

COPY . .
RUN pip install -r requirements.txt

# Run Python script
CMD [ "python", "main.py" ]
