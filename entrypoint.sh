#!/bin/sh
# Wait for DB to be ready, then run migrations
alembic upgrade head
# Start the app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000