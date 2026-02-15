from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.database import get_db


router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    response_model=UserResponse
)

def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.create_user(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
