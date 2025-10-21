# Use the official Python image from Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8080

# Set the environment variable to indicate that Flask is running in production
ENV FLASK_ENV=production

# Define the default command to run the application
CMD ["python", "app.py"]
