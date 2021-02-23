from sqlalchemy import Column, Date, BigInteger, String
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class School(Base, TimestampMixin):
    __tablename__ = "Schools"
    id = Column("Id", BigInteger, primary_key=True, index=True)
    name = Column("Name", String(128))
    established_date = Column("EstablishedDate", Date)
    address = Column("Address", String(512))
    students = relationship("Student", back_populates="school")
    grades = relationship("Grade", back_populates="school")
