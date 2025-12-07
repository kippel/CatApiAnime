# Use a multi-stage build for efficiency
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy project configuration files
COPY pyproject.toml uv.lock ./

# Install dependencies using the frozen lockfile
# --no-install-project: minimal install for dependencies only
RUN uv sync --frozen --no-install-project

# Copy the rest of the application code
COPY app ./app

# Expose port 80
EXPOSE 4000

# Run the application
# We use `uv run` to ensure we're using the environment created by uv
CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port", "4000", "--host", "0.0.0.0"]
