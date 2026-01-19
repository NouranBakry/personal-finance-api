from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy import create_engine
from app.config import settings  # Import your new settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()  # 1. Create a session
    try:
        yield db         # 2. Hand it to the API route
    finally:
        db.close()       # 3. Always close it, no matter what happens
