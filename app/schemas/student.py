import datetime

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    name: str
    gender: bool
    dob: datetime.date
    email: EmailStr
    grade_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentDbBase(StudentBase):
    id: int

    class Config:
        orm_mode = True


class Student(StudentDbBase):
    pass
