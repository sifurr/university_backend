from pydantic import BaseModel, EmailStr
from enum import Enum


class UserRoleEnum(str, Enum):
    admin = "admin"
    faculty = "faculty"
    student = "student"


class UserCreate(BaseModel):
    """
    Input schema for user creation.
    """
    full_name: str
    email: EmailStr
    password: str
    role: UserRoleEnum | None = None


class UserResponse(BaseModel):
    """
    Output schema.
    Never expose password.
    """
    id: int
    full_name: str
    email: EmailStr
    role: UserRoleEnum
    is_active: bool

    class Config:
        # This allows Pydantic to read data from ORM objects directly.
        from_attributes = True 
    

