from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Grade(Base):
    __tablename__ = "Grades"
    id = Column("Id", Integer, primary_key=True, index=True)
    name = Column("Name", String)
    students = relationship("Student", back_populates="grade")
    school_id = Column("SchoolId", Integer, ForeignKey("Schools.Id"))
    school = relationship("School", back_populates="grades")
