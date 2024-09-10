FROM python:3.12.5

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application (this is optional depending on how you'd like to start it)
# CMD ["python", "app.py"]
