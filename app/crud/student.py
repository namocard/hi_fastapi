from app import schemas, models
from app.crud.base import CRUDBase


class CRUDStudent(CRUDBase[models.Student, schemas.SchoolCreate, schemas.StudentUpdate]):
    pass


student = CRUDStudent(models.Student)
