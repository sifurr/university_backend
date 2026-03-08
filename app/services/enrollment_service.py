from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.enrollment import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.schemas.enrollment import EnrollmentCreate


class EnrollmentService:

    @staticmethod
    def enroll_student(db: Session, student_id: int, payload: EnrollmentCreate):

        existing = EnrollmentRepository.get_by_student_course(
            db, student_id, payload.course_id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Student already enrolled in this course!"
            )

        enrollment = Enrollment(
            student_id = student_id,
            course_id=payload.course_id
        )

        return EnrollmentRepository.create(db, enrollment)
    
    
    @staticmethod
    def get_student_courses(db: Session, student_id: int):

        return EnrollmentRepository.get_student_courses(db, student_id)
    
    


