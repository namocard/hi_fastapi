from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class School(Base):
    id = Column("Id", Integer, primary_key=True, index=True)
    name = Column("Name", String(128))
    established_date = Column("EstablishedDate", Date)
    address = Column("Address", String(512))
    students = relationship("Student", back_populates="students")
    grades = relationship("Grade", back_populates="school")