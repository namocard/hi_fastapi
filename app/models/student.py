from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Student(Base):
    __tablename__ = "Students"
    id = Column("Id", Integer, primary_key=True, index=True)
    name = Column("Name", String)
    gender = Column("Gender", Boolean)
    dob = Column("Date", Date)
    email = Column(String, unique=True)
    grade_id = Column("GradeId", Integer, ForeignKey("Grades.Id"))
    grade = relationship("Grade", back_populates="students")
    school_id = Column("SchoolId", Integer, ForeignKey("Schools.Id"))
    school = relationship("School", back_populates="students")
