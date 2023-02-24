FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update
RUN apt -y upgrade
RUN apt -y install python3-pip
RUN apt-get -y install libnss3 libatk-bridge2.0-0 libdrm-dev libxkbcommon-dev libgbm-dev libasound-dev libatspi2.0-0 libxshmfence-dev
RUN apt -y install build-essential libssl-dev libffi-dev python3-dev

COPY . /app

RUN pip install playwright
RUN pip install pymongo
RUN playwright install chromium
RUN playwright install-deps
# Run the command to start the app
CMD ["python3", "main.py"]