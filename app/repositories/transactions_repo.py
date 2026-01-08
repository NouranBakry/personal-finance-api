from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Transaction, Account


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, transaction_id: int):
        query = select(Transaction).where(Transaction.id == transaction_id)
        result = self.db.execute(query)
        return result.scalars().first()

    def create(self, transaction_model: Transaction):
        self.db.add(transaction_model)
        self.db.commit()
        self.db.refresh(transaction_model)
        return transaction_model

    def get_by_account(self, account_id: int):
        query = select(Transaction).where(Transaction.account_id == account_id)
        result = self.db.execute(query)
        return result.scalars().all()