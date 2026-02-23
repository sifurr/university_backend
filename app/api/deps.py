from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app.core.jwt import decode_token
from app.core.database import get_db
from app.models.user import User

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    """_
    Extract and validata JWT
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="invalid token")
    
    token = authorization.split(" ")[1]
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.id == payload["user_id"], User.is_active == True).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user
