from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from app.repositories.user_repo import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.schemas import UserCreate, UserRead
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

router = APIRouter(prefix="/auth", tags=["auth"])

def get_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return AuthService(user_repo)

@router.post("/register")
def register_user(userData: UserCreate, service: AuthService = Depends(get_service)):
    try:
        return service.register_user(userData)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)
    user = service.authenticate(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"},)
    
    access_token = service.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(AuthService.get_current_user)):
    return current_user