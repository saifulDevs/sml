# Use the official Python image
FROM python:3.10-slim
# Set working directory
WORKDIR /app
# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Copy the app code
COPY ./app ./app
# Run FastAPI app with Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]