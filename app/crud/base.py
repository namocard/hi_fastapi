from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import UnaryExpression

from app.db.base import Base
from app.core.identifier import generate_unique_int

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, session: Session, id: Any) -> Optional[ModelType]:
        return session.query(self.model).filter(self.model.id == id).first()

    @staticmethod
    def get_by_map(
        session: Session, model: ModelType, criteria_map: Dict[str, Any], order_by: UnaryExpression = None
    ) -> Optional[ModelType]:
        query = session.query(model)
        for attr, value in criteria_map.items():
            if hasattr(model, attr):
                if value is None:
                    query = query.filter(getattr(model, attr).is_(None))
                elif isinstance(value, (list, tuple)):
                    query = query.filter(getattr(model, attr).in_(value))
                else:
                    query = query.filter(getattr(model, attr) == value)
        if order_by is not None:
            query = query.order_by(order_by)
        return query.first()

    def get_multi(self, session: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return session.query(self.model).offset(skip).limit(limit).all()

    @staticmethod
    def get_multi_by_map(
        session: Session,
        model: ModelType,
        criteria_map: Dict[str, Any],
        order_by: UnaryExpression = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Optional[ModelType]:
        query = session.query(model)
        for attr, value in criteria_map.items():
            if hasattr(model, attr):
                if value is None:
                    query = query.filter(getattr(model, attr).is_(None))
                elif isinstance(value, (list, tuple)):
                    query = query.filter(getattr(model, attr).in_(value))
                else:
                    query = query.filter(getattr(model, attr) == value)
        if order_by is not None:
            query = query.order_by(order_by)
        if skip:
            query = query.offset(skip)
        if limit:
            query = query.limit(limit)
        return query.all()

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db_obj.id = generate_unique_int()
        session.add(db_obj)
        return db_obj

    def update(
        self, session: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        return db_obj

    def remove(self, session: Session, *, id: int) -> ModelType:
        obj = session.query(self.model).get(id)
        session.delete(obj)
        session.commit()
        return obj
