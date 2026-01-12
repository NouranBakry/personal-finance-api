from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost:5432/finance_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()  # 1. Create a session
    try:
        yield db         # 2. Hand it to the API route
    finally:
        db.close()       # 3. Always close it, no matter what happens
