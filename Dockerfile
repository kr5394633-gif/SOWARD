# Multi-stage Docker build for SowardBot
# Stage 1: Build React dashboard
FROM node:18-alpine AS dashboard-builder

WORKDIR /app/dashboard

COPY dashboard/package*.json ./
RUN npm ci

COPY dashboard/ .
RUN npm run build

# Stage 2: Build final application
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Copy pre-built React dashboard from stage 1
COPY --from=dashboard-builder /app/dashboard/build ./dashboard/build

# Create logs directory
RUN mkdir -p logs

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:3000/health')" || exit 1

# Run the application
# Secrets (TOKEN, DATABASE_URL, etc.) come from environment variables set by Railway
CMD ["python", "launcher.py"]
