# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files to the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
