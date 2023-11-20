# Use the official Python image as the base image
FROM python:3.8.10

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask server will run
EXPOSE 5000

# Command to run the application
CMD ["python3", "server.py"]