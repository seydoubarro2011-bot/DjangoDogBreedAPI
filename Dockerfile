# Use Python 3.11 as the base image
FROM python:3.11-slim

# Prevent Python from creating bytecode files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install Django and all required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Document the Django application port
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]