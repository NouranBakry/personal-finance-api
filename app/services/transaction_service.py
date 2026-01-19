from decimal import Decimal
from fastapi import HTTPException
from app.models import Account, Transaction
from datetime import datetime
from sqlalchemy import func, extract

class TransactionService:
    def __init__(self, db):
        self.db= db

    def create_transaction(self, account_id: int, user_id: int, amount: Decimal, description: str):
        # Logic to create a transaction in the database
        account = self.db.query(Account).filter(Account.id == account_id, Account.user_id == user_id).first()
        if not account:
            raise HTTPException(status_code= 400, detail="Account not found or does not belong to user")
        try:
            new_tx = Transaction(
                account_id=account_id,
                amount=amount,
                description=description
            )
            self.db.add(new_tx)
            self.db.commit()
            self.db.refresh(new_tx)
            return new_tx
        
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error creating transaction")

    def get_transaction(self, transaction_id):
        # Logic to retrieve a transaction from the database
        pass

    def delete_transaction(self, transaction_id):
        # Logic to delete a transaction from the database
        pass
    
    def get_monthly_summary(self, user_id: int):
        now = datetime.utcnow()
        
        total_balance = self.db.query(func.sum(Account.balance))\
            .filter(Account.user_id == user_id).scalar() or 0
            
        # sum of positive transactions for the current month    
        monthly_income = self.db.query(func.sum(Transaction.amount))\
            .join(Account)\
            .filter(
            Account.user_id == user_id,
            Transaction.amount > 0,
            extract('month', Transaction.created_at) == now.month,
            extract('year', Transaction.created_at) == now.year
        ).scalar() or 0

        # sum of negative transactions for the current month
        monthly_expenses = self.db.query(func.sum(Transaction.amount))\
            .join(Account)\
            .filter(
            Account.user_id == user_id,
            Transaction.amount < 0,
            extract('month', Transaction.created_at) == now.month,
            extract('year', Transaction.created_at) == now.year
        ).scalar() or 0
            
        return {
            "total_balance": total_balance,
            "monthly_income": monthly_income,
            # Show as positive number
            "monthly_expenses": abs(monthly_expenses),
            "net_savings": monthly_income + monthly_expenses
        }
