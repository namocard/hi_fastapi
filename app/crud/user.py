from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app import models
from app import schemas
from app.core.identifier import generate_unique_int
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
    def create(self, session: Session, obj_in: schemas.UserCreate) -> models.User:
        db_obj = models.User(
            id=generate_unique_int(),
            username=obj_in.username,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        session.add(db_obj)
        return db_obj

    def update(
        self, session: Session, db_obj: models.User, obj_in: Union[schemas.UserUpdate, Dict[str, Any]]
    ) -> models.User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(session, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, session: Session, username: str, password: str) -> Optional[models.User]:
        user = self.get_by_map(session, models.User, {"username": username})
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: models.User) -> bool:
        return user.is_active

    def is_superuser(self, user: models.User) -> bool:
        return user.is_superuser


user = CRUDUser(models.User)
