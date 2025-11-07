# Use Python 3 Alpine as base image
FROM python:3-alpine

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user and switch to it
RUN adduser -D myuser
USER myuser

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]