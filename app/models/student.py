from sqlalchemy import Boolean, Column, Date, ForeignKey, BigInteger, String
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Student(Base, TimestampMixin):
    __tablename__ = "Students"
    id = Column("Id", BigInteger, primary_key=True, index=True)
    name = Column("Name", String)
    gender = Column("Gender", Boolean)
    dob = Column("Date", Date)
    email = Column(String, unique=True)
    grade_id = Column("GradeId", BigInteger, ForeignKey("Grades.Id"))
    grade = relationship("Grade", back_populates="students")
    school_id = Column("SchoolId", BigInteger, ForeignKey("Schools.Id"))
    school = relationship("School", back_populates="students")
