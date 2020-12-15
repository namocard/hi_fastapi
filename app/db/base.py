from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class TimestampMixin:
    created_at = Column("CreatedAt", DateTime, nullable=False, server_default=func.now())
    updated_at = Column("UpdatedAt", DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())
