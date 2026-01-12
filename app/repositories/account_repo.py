from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Account
from decimal import Decimal

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, account_id: int):
        query = select(Account).where(Account.id == account_id)
        result = self.db.execute(query)
        return result.scalars().first()

    def get_all_by_user(self, user_id: int):
        # Audit-Ready: Only fetch accounts belonging to THIS user
        query = select(Account).where(Account.user_id == user_id)
        return self.db.execute(query).scalars().all()
    
    def create(self, account_model: Account):
        self.db.add(account_model)
        self.db.commit()
        self.db.refresh(account_model)
        return account_model

    def update_balance(self, account_id: int, amount: Decimal):
        account = self.get_by_id(account_id)    
        if account:
            account.balance += amount
            self.db.commit()
            self.db.refresh(account)
        return account