from app.models import User, Account, Transaction
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy import create_engine
from app.config import settings  # Import your new settings
from .base import Base

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=3600, pool_timeout=30)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()  # 1. Create a session
    try:
        yield db         # 2. Hand it to the API route
    finally:
        db.close()       # 3. Always close it, no matter what happens
