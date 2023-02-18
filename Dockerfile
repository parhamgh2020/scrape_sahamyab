FROM mcr.microsoft.com/playwright:v1.30.0-focal

# Install any necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Start the app
CMD [ "python3", "app.py" ]
