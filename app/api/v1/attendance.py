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