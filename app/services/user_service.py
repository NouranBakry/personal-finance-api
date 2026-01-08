from passlib.context import CryptContext
from app.repositories.user_repo import UserRepository
from app.models import User
from app.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserService: 
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def register_user(self, userData: UserCreate):
        
        existing_user = self.user_repo.get_by_email(userData.email)
        if existing_user:
            raise Exception("User with this email already exists.")
        
        hashed_password = self.hash_password(userData.password)
        new_user = User(
            email=userData.email,
            hashed_password=hashed_password,
            is_active=True
        )
        return self.user_repo.create(new_user)
    
    