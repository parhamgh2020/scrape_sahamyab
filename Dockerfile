FROM python:3.9-slim-buster

ENV TZ="Africa/Lusaka"

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    libglib2.0-0 \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libdrm2 \
    libgbm1 \
    libasound2 \
    fonts-noto-cjk \
    && rm -rf /var/lib/apt/lists/*

# Install the latest version of Playwright for Python
RUN curl -fsSL https://playwright.dev/python-cli | python -


WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python3", "main.py"]
