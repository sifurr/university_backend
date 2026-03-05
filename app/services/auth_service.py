from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password
from app.core.jwt import (
    create_access_token,
    create_refresh_token
)

import logging


security_logger = logging.getLogger("security")

class AuthService():
    """
    Handles authentication logic
    """

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserRepository.get_by_email(db, email)

        

        # User existence + soft delete check
        if not user:
            security_logger.warning(f"Login failed: unknown email -> {email}")
            raise ValueError("Invalid credentials")      
        
        if not user.is_active: 
            security_logger.warning(f"Login blocked: inactive user -> {email}")         
            raise ValueError("Invalid credentials")
        
        #Password verification
        if not verify_password(password, user.hashed_password):
            security_logger.warning(f"Login failed: wrong password -> {email}")  
            raise ValueError("Invalid  credentials")    


        # successful login
        security_logger.info(f"Successful login -> {user.email}")  

        # Token payload
        payload = {
            "user_id": user.id,
            "role": user.role.value
        }

        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload)
        }