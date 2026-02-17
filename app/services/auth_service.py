from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password
from app.core.jwt import (
    create_access_token,
    create_refresh_token
)


class AuthService():
    """
    Handles authentication logic
    """

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserRepository.get_by_email(db, email)

        # User existence + soft delete check
        if not user or not user.is_active:
            raise ValueError("Invalid credentials")
        
        # Token payload
        payload = {
            "user_id": user.id,
            "role": user.role.value
        }

        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload)
        }