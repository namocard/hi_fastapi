from typing import Any
import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.core.config import settings
from app.core.security import create_access_token
from app import schemas

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
async def get_access_token(
    *, session: Session = Depends(deps.get_session), form: OAuth2PasswordRequestForm = Depends()
) -> Any:
    print(form)
    db_user = crud.user.authenticate(session, username=form.username, password=form.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect user or password")
    if not db_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = schemas.Token(
        access_token=create_access_token(db_user.id, expires_delta=access_token_expires), token_type="bearer"
    )
    return token


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: schemas.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
