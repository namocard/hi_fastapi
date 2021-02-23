from typing import List
from fastapi import APIRouter

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps
from app import models

router = APIRouter()


@router.post("/", response_model=schemas.Grade)
async def create_grade(
    *,
    session: Session = Depends(deps.get_session),
    grade_in: schemas.GradeCreate,
    _: models.User = Depends(deps.get_current_active_superuser)
) -> schemas.Grade:
    db_school = crud.school.get_by_map(session, models.School, {"id": grade_in.school_id})
    if not db_school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School id does not exist")
    db_grade = crud.grade.create(session, obj_in=grade_in)
    grade = schemas.Grade.from_orm(db_grade)
    session.commit()
    return grade


@router.get("/", response_model=List[schemas.Grade])
async def read_grades(
    *,
    session: Session = Depends(deps.get_session),
    limit: int = 50,
    skip: int = 0,
    _: models.User = Depends(deps.get_current_active_user)
):
    return crud.grade.get_multi_by_map(session, models.Grade, {}, limit=limit, skip=skip)


@router.get("/{grade_id}", response_model=schemas.Grade)
async def read_grade(
    *,
    session: Session = Depends(deps.get_session),
    grade_id: int,
    _: models.User = Depends(deps.get_current_active_user)
) -> schemas.Grade:
    db_grade = crud.grade.get_by_map(session, models.Grade, {"id": grade_id})
    if db_grade:
        return db_grade
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade id does not exist")
