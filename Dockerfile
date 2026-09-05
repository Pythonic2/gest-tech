# Use a imagem oficial do Python
FROM python:3.14

# Set up the working directory
WORKDIR /app

EXPOSE 8001
# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Keep the startup script in the image independently of the application mount.
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy the rest of the application to the container
COPY . .

# Run the initialization commands before starting the application
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
