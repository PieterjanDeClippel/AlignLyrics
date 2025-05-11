FROM python:3.10-slim

# Install build dependencies and libraries
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libespeak-dev \
    git \
    curl \
    gcc \
    g++ \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir aeneas yt-dlp

# Set workdir
WORKDIR /app

# Copy your script and lyrics
COPY align.py .
COPY whatever.txt .
COPY never-gonna-give-you-up.txt .

ENTRYPOINT ["python", "align.py"]
CMD []