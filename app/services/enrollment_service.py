from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.core.exceptions import BadRequestException

from app.models.enrollment import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.schemas.enrollment import EnrollmentCreate

from app.repositories.course_repository import CourseRepository


class EnrollmentService:

    @staticmethod
    def enroll_student(db: Session, student_id: int, payload: EnrollmentCreate):

        try:
            existing = EnrollmentRepository.get_by_student_course(
                db, student_id, payload.course_id
            )

            if existing:
                return existing  # error na, existing return for Idempotent api design behavior
                # raise HTTPException(
                #     status_code=400,
                #     detail="Student already enrolled in this course!"
                # )

            enrollment = Enrollment(
                student_id = student_id,
                course_id=payload.course_id
            )
            
            EnrollmentRepository.create(db, enrollment)
            db.commit()
            db.refresh(enrollment)

            course = CourseRepository.get_for_update(db, payload.course_id)

            if not course:
                raise HTTPException(404, "Course not found")

            return enrollment
        
    
        except IntegrityError:
            db.rollback()

            existing = EnrollmentRepository.get_by_student_course(
                db, student_id, payload.course_id
            )

            if existing:
                return existing
            
            raise

            # raise HTTPException(
            #     status_code=400,
            #     detail="Student already enrollment in this course"
            # )
        
        # except Exception:
        #     db.rollback()
        #     raise
    
    
    @staticmethod
    def get_student_courses(db: Session, student_id: int):

        return EnrollmentRepository.get_student_courses(db, student_id)
    
    


