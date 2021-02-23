from typing import List
import datetime

from pydantic import BaseModel
from app.schemas.grade import Grade


class SchoolBase(BaseModel):
    name: str
    established_date: datetime.date
    address: str


class SchoolCreate(SchoolBase):
    pass


class SchoolUpdate(SchoolBase):
    pass


class SchoolDbBase(SchoolBase):
    id: int

    class Config:
        orm_mode = True


class School(SchoolDbBase):
    grades: List[Grade]
