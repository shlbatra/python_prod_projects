FROM python:3.13-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY fastapi_exchange_app/pyproject.toml fastapi_exchange_app/uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY fastapi_exchange_app .
