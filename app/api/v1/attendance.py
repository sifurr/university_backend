from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.attendance import AttendanceCreate
from app.services.attendance_service import AttendanceService
from app.api.deps import get_current_user
from app.core.permissions import require_role


router = APIRouter(prefix="/attendance", tags=["Attendance"])


#Teacher marks attendance
@router.post("/mark")
def mark_attendance(
    payload: AttendanceCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role(['faculty']))
):
    return AttendanceService.mark_attendance(db, payload)


# Student views own attendance
@router.get("/my")
def my_attendance(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
): 
    return AttendanceService.get_student_attendance(db, user.id)


@router.get("/percentage/{course_id}")
def attendance_percentage(
    course_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    percentage = AttendanceService.get_attendance_percentage(
        db, user.id, course_id
    )

    return {
        "course_id": course_id,
        "attendance_percentage": percentage
    }

@router.get("/course-report/{course_id}")
def course_report(
    course_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_role(['faculty']))
):
    
    return AttendanceService.get_course_report(db, course_id)


@router.get("/faculty-dashboard")
def teacher_dashboard(
    db: Session = Depends(get_db),
    user = Depends(require_role(['faculty']))
):
    return AttendanceService.teacher_dashboard(db, user.id)

