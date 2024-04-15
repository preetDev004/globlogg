# Use the Python 3.10 slim-buster base image (Stable & Lightweight)
FROM python:3.10-slim-buster

# Set the PYTHONUNBUFFERED environment variable to ensure Python output is sent straight to terminal (optional)
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]