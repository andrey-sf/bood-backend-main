# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install

RUN poetry add setuptools

# Set PYTHONPATH to include the current directory
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Expose port 8000
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
