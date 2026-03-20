from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.attendance import Attendance, AttendanceStatus



class AttendanceRepository:

    @staticmethod
    def create(db: Session, attendance: Attendance):
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        
        return attendance
    
    
    @staticmethod
    def get_student_attendance(db: Session, student_id: int):
        return db.query(Attendance).filter(Attendance.student_id == student_id).all()
    

    @staticmethod
    def get_by_unique_key(db, student_id, course_id, date):

        return db.query(Attendance).filter(
            Attendance.student_id == student_id,
            Attendance.course_id == course_id,
            Attendance.date == date
        ).first()
    

    @staticmethod
    def get_attendance_summary(db: Session, student_id: int, course_id: int):

        total = db.query(func.count(Attendance.id)).filter(
            Attendance.student_id == student_id,
            Attendance.course_id == course_id
        ).scalar()

        present = db.query(func.count(Attendance.id)).filter(
            Attendance.student_id == student_id,
            Attendance.course_id == course_id,
            Attendance.status == AttendanceStatus.PRESENT
        ).scalar()

        return total, present
    