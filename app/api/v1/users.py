from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.database import get_db

from app.core.permissions import require_role


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.create_user(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/admin-only")
def admin_endpoint(user = Depends(require_role(['admin']))):
    
    return {"message": "Only admin can access"}

@router.get("/teacher-area")
def teacher_endpoint(user = Depends(require_role(['faculty', 'admin']))):
    return {"message": "Teacher or Admin allowed"}


@router.get("/student-area")
def student_endpoint(user = Depends(require_role(['student']))):
    return {"message": "only student allowed"}