from sqlalchemy import Column, Boolean, DateTime, func
from app.core.database import Base
# from app.models.course import Course
# from app.models.enrollment import Enrollment
# from app.models.attendance import Attendance


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
