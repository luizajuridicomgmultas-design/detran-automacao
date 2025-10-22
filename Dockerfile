FROM python:3.11-slim

WORKDIR /app

# Instala somente o mínimo necessário para Playwright/Chromium headless
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libxss1 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libasound2 \
    libdbus-glib-1-2 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install

COPY . .

CMD ["python", "processar_lote.py"]

