from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    """
    Handles ONLY database operations.
    """

    @staticmethod
    def get_by_email(db: Session, email: str):        
        return(db.query(User).filter(User.email == email, User.is_active == True).first())
    
    @staticmethod
    def create(db: Session, user: User):
        db.add(user)
        db.flush() # assign ID without commit
        return user
    
  