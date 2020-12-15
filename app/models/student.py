from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Student(Base):
    id = Column("Id", Integer, primary_key=True, index=True)
    name = Column("Name", String)
    gender = Column("Gender", Boolean)
    dob = Column("Date", Date)
    email = Column(String, unique=True)
    grade = relationship("Grade", back_populates="grade")
    school = relationship("School", back_populates="school")
