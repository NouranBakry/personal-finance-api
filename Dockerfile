FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]

# Install system dependencies (psycopg2 needs these)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# We will override this CMD in docker-compose for migrations
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]