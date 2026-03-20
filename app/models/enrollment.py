from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Enrollment(BaseModel):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    student = relationship("User")
    course = relationship("Course")
    
    __table_args__ = (
        UniqueConstraint("student_id", "course_id", name="unique_student_course"),
    )
    
    