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
    username: str
    

class Config:
    from_attributes = True  # This allows Pydantic to read SQLAlchemy objects
    
class AccountCreate(BaseModel):
    name: str
    initial_balance: Decimal = 0.0
    
class AccountRead(BaseModel):
    uuid: str
    name: str
    balance: Decimal
    created_at: datetime
    owner_id: int
    
class TransactionCreate(BaseModel):
    amount: Decimal
    account_uuid: str
    
class TransactionRead(BaseModel):
    id: int
    amount: Decimal
    created_at: datetime
    
class Token(BaseModel):
    access_token: str
    token_type: str #Usually "bearer"
    
class TokenData(BaseModel):
    # This is what's hidden INSIDE the token (usually the user's ID or email)
    username: Optional[str] = None
    class Config:
        from_attributes = True  # This allows Pydantic to read SQLAlchemy objects
        
class MonthlySummary(BaseModel):
    total_balance: Decimal
    monthly_income: Decimal
    monthly_expenses: Decimal
    net_savings: Decimal