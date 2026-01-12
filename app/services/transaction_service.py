from decimal import Decimal
from fastapi import HTTPException
from app.models import Account, Transaction

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