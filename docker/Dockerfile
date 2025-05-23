FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

COPY docker/requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "/app/src/main.py"]
