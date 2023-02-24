FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

# Add python script to Docker
COPY . .
RUN apt install python3-pip
RUN pip install -r requirements.txt
RUN pip install pytest-playwright

# Run Python script
CMD [ "python", "main.py" ]
