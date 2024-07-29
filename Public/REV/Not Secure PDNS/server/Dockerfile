# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./server.py ./server.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask pycryptodome

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run server.py when the container launches
CMD ["python", "server.py"]
