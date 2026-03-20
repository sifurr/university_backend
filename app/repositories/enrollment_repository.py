from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment


class EnrollmentRepository:

    @staticmethod
    def create(db: Session, enrollment: Enrollment):

        db.add(enrollment)
        db.flush() # commit na, only db a push
        # db.commit()
        # db.refresh(enrollment)

        return enrollment
    
    @staticmethod
    def get_student_courses(db: Session, student_id: int):

        return db.query(Enrollment).filter(
            Enrollment.student_id == student_id
        ).all()
    
    @staticmethod
    def get_by_student_course(db: Session, student_id: int, course_id: int):

        return db.query(Enrollment).filter(
            Enrollment.student_id == student_id,
            Enrollment.course_id == course_id
        ).first()
    
    
