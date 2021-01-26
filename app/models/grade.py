from sqlalchemy import Column, ForeignKey, BigInteger, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Grade(Base):
    __tablename__ = "Grades"
    id = Column("Id", BigInteger, primary_key=True, index=True)
    name = Column("Name", String)
    students = relationship("Student", back_populates="grade")
    school_id = Column("SchoolId", BigInteger, ForeignKey("Schools.Id"))
    school = relationship("School", back_populates="grades")
