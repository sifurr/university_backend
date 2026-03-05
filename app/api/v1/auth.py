
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.core.database import get_db

from app.api.deps import get_current_user
from app.core.security import hash_password, verify_password
from app.schemas.password import ChangePasswordRequest



router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/change-password")
def change_password(payload: ChangePasswordRequest, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    if not verify_password(payload.old_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Old password incorrect")
    
    current_user.hashed_password = hash_password(payload.new_password)

    return {"message": "Password updated successfully"}



@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        tokens = AuthService.login(db, payload.email, payload.password)        
        
        return tokens
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    
    