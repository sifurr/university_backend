from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.models.base import BaseModel
import enum


class UserRole(enum.Enum):
    """
    Enprise role system.
    Extendable in future
    """
    ADMIN = "admin"
    FACULTY = "faculty"
    STUDENT = "student"

class User(BaseModel):
    """
    User table.
    Inherits:
    - is_active
    - created_at
    - updated_at
    """              
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(
        Enum(UserRole),
        default=UserRole.STUDENT,
        nullable=False
    )
    is_verified = Column(Boolean, default=False)
    
