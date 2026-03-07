from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    faculty_id: Optional[int] = None

class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    description: Optional[str]
    faculty_id: Optional[int]

    class Config:
        from_attribute = True
    

