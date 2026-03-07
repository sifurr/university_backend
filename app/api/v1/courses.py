from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.course import CourseCreate, CourseResponse
from app.services.course_service import CourseService
from app.core.permissions import require_role

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/")
def create_course(
    payload: CourseCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role(["admin"]))
):
    
    return CourseService.create_course(db, payload)


@router.get("/", response_model=list[CourseResponse])
def get_course(db: Session = Depends(get_db)):

    return CourseService.get_courses(db)