FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libasound2-dev \
    ffmpeg \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .

RUN sed -i '/torch/d' requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/Database && chmod 777 /app/Database

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]