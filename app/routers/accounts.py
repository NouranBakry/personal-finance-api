from fastapi import APIRouter, Depends
from app.database import get_db, Session
from app.repositories.account_repo import AccountRepository
from app.services.account_service import AccountService
from app.routers.auth import read_users_me
from app.models import User
from app.schemas import AccountCreate, AccountRead


router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/", response_model=AccountRead)
def create_account(
    account_data: AccountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(read_users_me)  # PROTECTED
):
    repo = AccountRepository(db)
    service = AccountService(repo)
    return service.create_account(account_data, current_user.id)
