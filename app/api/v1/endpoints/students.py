from typing import List
from fastapi import APIRouter

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Student)
async def create_student(
    *,
    session: Session = Depends(deps.get_session),
    schema_in: schemas.StudentCreate,
    _: models.User = Depends(deps.get_current_active_superuser)
) -> schemas.Student:
    db_grade = crud.grade.get_by_map(session, models.Grade, {"id": schema_in.grade_id})
    if not db_grade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade id does not exist")
    db_student = crud.student.create(session, obj_in=schema_in)
    session.commit()
    return db_student


@router.get("/", response_model=List[schemas.Grade])
async def read_students(
    *, session: Session = Depends(deps.get_session), _: models.User = Depends(deps.get_current_active_user)
):
    return crud.student.get_multi(session, skip=0, limit=10)
