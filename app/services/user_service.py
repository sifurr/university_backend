from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User, UserRole
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password


class UserService:
    """
    Business logic layer
    """

    @staticmethod
    def create_user(db: Session, data: UserCreate):
        # prevent duplicate email
        existing = UserRepository.get_by_email(
            db,
            data.email
        )
        if existing:
            raise ValueError("Email already registered")
        
        # hash password
        hashed_pw = hash_password(data.password)
        
        # assign role safely
        role = (
            UserRole(data.role)
            if data.role       
            else UserRole.STUDENT
        )

        user = User(
            full_name = data.full_name,
            email = data.email,
            hashed_password = hashed_pw,
            role = role
        )

        return UserRepository.create(db, user)