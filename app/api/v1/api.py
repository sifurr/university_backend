from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as user_router
from app.api.v1.courses import router as course_router
from app.api.v1.enrollments import router as enrollment_router
from app.api.v1.attendance import router as attendance_router


router = APIRouter(prefix="/api/v1")

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(course_router)
router.include_router(enrollment_router)
router.include_router(attendance_router)

