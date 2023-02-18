FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

WORKDIR /app

COPY requirements.txt requirements
RUN pip install -r requirements.txt

RUN playwright install --with-deps chromium

CMD ["python3", "main.py"]