from sqlalchemy import Boolean, Column, BigInteger, String

from app.db.base import Base


class User(Base):
    __tablename__ = "Users"
    id = Column("Id", BigInteger, primary_key=True, index=True)
    username = Column("Username", String, index=True, unique=True, nullable=False)
    hashed_password = Column("HashedPassword", String, nullable=False)
    full_name = Column("FullName", String)
    email = Column("Email", String, unique=True, index=True, nullable=False)
    is_active = Column("IsActive", Boolean(), default=True)
    is_superuser = Column("IsSuperUser", Boolean(), default=False)
