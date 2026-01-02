from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    username: str
    
class UserCreate(UserBase):
    password: str
    
class UserRead(UserBase):
    id: int
    uuid: str
    created_at: datetime
    

class Config:
    from_attributes = True  # This allows Pydantic to read SQLAlchemy objects
