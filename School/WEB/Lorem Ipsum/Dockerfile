# Use an official Python 3 image as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

RUN mkdir templates

# Copy the application files from the host into the container
COPY app.py /app/
COPY templates/index.html /app/templates/
COPY fl4g.txt /fl4g.txt

# Install required dependencies
RUN pip install Flask Jinja2

# Expose port 5000 to access the application
EXPOSE 5000

# Start the application
CMD ["python3", "app.py"]
