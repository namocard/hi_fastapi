from typing import List
from fastapi import APIRouter

from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.school import SchoolCreate, School

router = APIRouter()


@router.post("/", response_model=School)
async def create_school(*, session: Session = Depends(deps.get_session), school_in: SchoolCreate) -> School:
    db_school = crud.school.create(session, obj_in=school_in)
    session.commit()
    return db_school


@router.get("/", response_model=List[School])
async def read_schools(session: Session = Depends(deps.get_session)):
    return crud.school.get_multi(session, skip=0, limit=10)
