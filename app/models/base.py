from sqlalchemy import Column, Boolean, DateTime, func
from app.core.database import Base


class BaseModel(Base):
    """
    Abstract base model.
    Implements:
    - Soft delete
    - Audit timestamps
    """

    __abstract__ = True

    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )
