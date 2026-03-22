from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.attendance import Attendance, AttendanceStatus
from app.repositories.attendance_repository import AttendanceRepository
from app.schemas.attendance import AttendanceCreate


class AttendanceService:
    
    @staticmethod
    def mark_attendance(db: Session, payload: AttendanceCreate):
        try:
            existing = AttendanceRepository.get_by_unique_key(
                db,
                payload.student_id,
                payload.course_id,
                payload.date
            )

            if existing:
                raise HTTPException(
                    status_code=400,
                    detail="Attendance already marked for this date"
                )
            
            attendance = Attendance(
                student_id=payload.student_id,
                course_id=payload.course_id,
                date=payload.date,
                status=AttendanceStatus(payload.status)
            )

            return AttendanceRepository.create(db, attendance)

        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                details="Duplicate attendance detected"
            )
        
        except Exception as e:
            db.rollback()
            raise e
        
    
    @staticmethod
    def get_student_attendance(db: Session, student_id: int):
        return AttendanceRepository.get_student_attendance(db, student_id)
    

    @staticmethod
    def get_attendance_percentage(db, student_id: int, course_id: int):

        total, present = AttendanceRepository.get_attendance_summary(
            db, student_id, course_id
        )

        if total == 0:            
            return 0

        percentage = (present / total) * 100
        
        return round(percentage, 2)

    
    @staticmethod
    def get_course_report(db, course_id: int):

        data = AttendanceRepository.get_course_attendance_report(db, course_id)

        report = []

        for row in data:
            percentage = (row.present / row.total) * 100 if row.total else 0

            report.append({
                "student_id": row.student_id,
                "attendance_percentage" : round(percentage, 2)
            })
    
        return report
    

    @staticmethod
    def teacher_dashboard(db, teacher_id: int):
        total_students = db.query(Attendance.student_id).distinct().count()

        total_classes = db.query(Attendance.date).distinct().count()

        total_present = db.query(Attendance).filter(
            Attendance.status == AttendanceStatus.PRESENT
        ).count()

        return {
            "total_status": total_students,
            "total_classes": total_classes,
            "total_present_records": total_present
        }


        
