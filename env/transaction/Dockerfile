# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /usr/local/app

# Copy the current directory contents into the container at /app
COPY . ./


# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

#Maybe cmd for good practice for blocking processes
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
