from sqlalchemy import Column, Integer, ForeignKey, Date, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel


class AttendanceStatus(enum.Enum):
    PRESENT = "present"
    ABSENT = "absent"

class Attendance(BaseModel):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), nullable=False)

    student = relationship("User")
    course = relationship("Course")

    __table_args__ = (
        UniqueConstraint("student_id", "course_id", "date", name="unique_attendance"),
    )
