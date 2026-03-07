from sqlalchemy.orm import Session

from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course import CourseCreate


class CourseService:
    
    @staticmethod
    def create_course(db: Session, payload: CourseCreate):

        course = Course(
            name=payload.name,
            code=payload.code,
            description=payload.description,
            faculty_id=payload.faculty_id
        )

        return CourseRepository.create(db, course)
    

    @staticmethod
    def get_courses(db: Session):

        return CourseRepository.get_all(db)
    