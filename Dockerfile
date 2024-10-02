# Use the Ubuntu base image
FROM ubuntu

# Set working directory inside the container
WORKDIR /app

# Copy requirements and project files into the container
COPY requirements.txt /app
COPY devops /app

# Install Python and the venv module
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Expose the port your Django app will run on
EXPOSE 8000

# Command to activate venv and run the server
CMD ["sh", "-c", ". venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]


# FROM ubuntu

# WORKDIR /app

# COPY requirements.txt /app
# COPY devops /app

# RUN apt-get update && \
#     apt-get install -y python3 python3-pip && \
#     pip install -r requirements.txt && \
#     cd devops

# ENTRYPOINT ["python3"]
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
