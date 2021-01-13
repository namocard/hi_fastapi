from sqlalchemy.orm import Session
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_students(session: Session):
    pass