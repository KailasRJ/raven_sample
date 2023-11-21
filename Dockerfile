# Use the official Python image as the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt


# Copy the application files to the container
COPY . .


# Expose the port on which the Flask server will run
EXPOSE 5000

# Command to run the application
CMD ["python3", "server.py"]
