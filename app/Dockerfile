# Base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code and the model file
COPY . .

# Expose the application port
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Define the command to run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
