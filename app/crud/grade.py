from app import models, schemas
from app.crud.base import CRUDBase


class CRUDGrade(CRUDBase[models.Grade, schemas.GradeCreate, schemas.GradeUpdate]):
    pass


grade = CRUDGrade(models.Grade)
