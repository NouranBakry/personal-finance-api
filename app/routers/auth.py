from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from app.repositories.user_repo import UserRepository
from app.services.user_service import UserService, AuthService
from app.schemas import UserCreate, UserRead


router = APIRouter(prefix="/auth", tags=["auth"])

def get_user_service(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return UserService(user_repo)

@router.post("/register")
def register_user(userData: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.register_user(userData)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = UserService(repo)
    
    user = repo.get_by_email(form_data.username)
    if not user or not service.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"},)
    
    access_token = service.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(AuthService.get_current_user)):
    return current_user