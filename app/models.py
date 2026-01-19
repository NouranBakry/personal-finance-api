from decimal import Decimal
import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Numeric, Boolean
from sqlalchemy.orm import relationship
from .database import Base  # Import the Base from your database module
import uuid
from datetime import datetime

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    is_active = Column(Boolean, default=True)

class User (Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    uuid = Column(String, unique=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    accounts = relationship("Account", back_populates="owner")


class Account (Base, TimestampMixin):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    balance = Column(Numeric(precision=18, scale=2), default=0.0)

    user_id = Column(Integer, ForeignKey("users.id"))  # Assuming a user_id field for ownership
    
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction (Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(precision=18, scale=2))

    account_id = Column(Integer, ForeignKey("accounts.id"))  # Link to Account
    created_at = Column(DateTime, default=datetime.now())

    account = relationship("Account", back_populates="transactions")
