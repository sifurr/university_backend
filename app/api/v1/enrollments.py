from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.enrollment import EnrollmentCreate
from app.services.enrollment_service import EnrollmentService
from app.api.deps import get_current_user
from app.core.permissions import require_role


router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("/")
def enroll_course(
    payload: EnrollmentCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role(['student']))
    ):
    
    return EnrollmentService.enroll_student(db, user.id, payload)


@router.get("/my-courses")
def my_courses(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    
    return EnrollmentService.get_student_courses(db, user.id)


