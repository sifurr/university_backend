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
        ).scalar() or 0

        present = db.query(func.count(Attendance.id)).filter(
            Attendance.student_id == student_id,
            Attendance.course_id == course_id,
            Attendance.status == AttendanceStatus.PRESENT
        ).scalar() or 0

        print(f"DEBUG: Student {student_id}, Course {course_id} -> Total: {total}, Present: {present}")

        return total, present
    

    @staticmethod
    def get_course_attendance_report(db: Session, course_id: int):
        
        results = db.query(
            Attendance.student_id,
            func.count(Attendance.id).label("total"),
            func.sum(
                func.case(
                    (Attendance.status == AttendanceStatus.PRESENT, 1), 
                    else_=0
                )
            ).label("present")
        ).filter(
            Attendance.course_id == course_id
        ).group_by(Attendance.student_id).all()

        return results
    