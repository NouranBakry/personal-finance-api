
from app.models import Account
from app.repositories.account_repo import AccountRepository
from app.schemas import AccountCreate


class AccountService:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo
        
    def create_account(self, account_data: AccountCreate, user_id: int):
        new_account = Account (
            name=account_data.name,
            balance=account_data.initial_balance,
            user_id=user_id,
            is_active=True
        )
        return self.account_repo.create(new_account)
    
    