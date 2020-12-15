from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Grade(Base):
    id = Column("Id", Integer, primary_key=True, index=True)
    name = Column("Name", String)
    students = relationship("Student", back_populates="grade")
    school = relationship("School", back_populates="grades")
