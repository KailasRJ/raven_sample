# Use the official Python image as the base image
FROM python:3.10.1

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install MySQL development dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install -r requirements.txt


# Copy the application files to the container
COPY . .


# Expose the port on which the Flask server will run
EXPOSE 5000

# Command to run the application
CMD ["python3", "server.py"]
