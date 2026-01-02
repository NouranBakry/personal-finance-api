from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        # Using the modern SQLAlchemy 2.0 syntax
        query = select(User).where(User.email == email)
        result = self.db.execute(query)
        return result.scalars().first()

    def create(self, user_model: User):
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model
