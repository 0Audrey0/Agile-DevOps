# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies into a temporary directory
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-alpine

# Create a non-root user
RUN adduser -D myuser
USER myuser

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /home/myuser/.local
COPY --from=builder /app /app

# Update PATH to include the user's local bin
ENV PATH=/home/myuser/.local/bin:$PATH

COPY app /app/app

EXPOSE 5000

CMD ["python", "-m", "app.main"]
