from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.transactions_repo import TransactionRepository
from app.database import get_db
from app.models import User
from app.schemas import TransactionCreate, TransactionRead
from app.services.transaction_service import TransactionService
from app.routers.auth import read_users_me


router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=TransactionRead)
def create_transaction(transactionData: TransactionCreate, db: Session = Depends(get_db),     
                       current_user: User = Depends(read_users_me)):
    service = TransactionService(db)
    return service.create_transaction(account_id=transactionData.account_id, user_id=current_user.id, amount=transactionData.amount,description=transactionData.description)
    
@router.get("/monthly-summary")   
def get_monthly_summary(db: Session = Depends(get_db),     
                       current_user: User = Depends(read_users_me)):
    service = TransactionService(db)
    return service.get_monthly_summary(user_id=current_user.id)