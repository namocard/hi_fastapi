from typing import List
from fastapi import APIRouter

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps
from app import models

router = APIRouter()


@router.post("/", response_model=schemas.School)
async def create_school(
    *,
    session: Session = Depends(deps.get_session),
    school_in: schemas.SchoolCreate,
    _: models.User = Depends(deps.get_current_active_superuser)
) -> schemas.School:
    db_school = crud.school.create(session, obj_in=school_in)
    session.commit()
    return db_school


@router.get("/{school_id}", response_model=schemas.School)
async def read_school(
    *,
    session: Session = Depends(deps.get_session),
    school_id: int,
    _: models.User = Depends(deps.get_current_active_user)
) -> schemas.School:
    db_school = crud.student.get_by_map(session, models.School, {"id": school_id})
    if db_school:
        return db_school
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School id does not exist")


@router.get("/{school_id}/grades", response_model=List[schemas.Grade])
async def read_grades(
    *,
    session: Session = Depends(deps.get_session),
    school_id: int,
    _: models.User = Depends(deps.get_current_active_user)
) -> List[schemas.Grade]:
    db_school = crud.school.get_by_map(session, models.School, {"id": school_id})
    if not db_school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School id does not exist")
    return db_school.grades


@router.get("/", response_model=List[schemas.School])
async def read_schools(
    *, session: Session = Depends(deps.get_session), _: models.User = Depends(deps.get_current_active_user)
):
    return crud.school.get_multi(session, skip=0, limit=10)
