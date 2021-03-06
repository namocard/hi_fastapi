from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from fastapi import status

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/admin", response_model=schemas.User)
def create_admin_user(*, session: Session = Depends(deps.get_session), user_in: schemas.AdminUserCreate) -> Any:
    if user_in.secret_key != settings.SECRET_KEY:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The secret key is not correct")
    db_user = crud.user.get_by_map(session, models.User, {"username": user_in.username})
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system",
        )
    db_user = crud.user.get_by_map(session, models.User, {"username": user_in.username})
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="The email address has been used",
        )
    user_in.is_superuser = True
    db_user = crud.user.create(session, obj_in=user_in)
    session.commit()
    return db_user


@router.get("/", response_model=List[schemas.User])
def read_users(
    session: Session = Depends(deps.get_session),
    skip: int = 0,
    limit: int = 100,
    _: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi_by_map(session, models.User, {}, limit=limit, skip=skip)
    return users


@router.post("/", response_model=schemas.User)
def create_user(*, session: Session = Depends(deps.get_session), user_in: schemas.UserCreate) -> Any:
    """
    Create new user.
    """
    db_user = crud.user.get_by_map(session, models.User, {"username": user_in.username})
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system",
        )
    db_user = crud.user.get_by_map(session, models.User, {"email": user_in.email})
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The email address has been used",
        )
    db_user = crud.user.create(session, obj_in=user_in)
    session.commit()
    return db_user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    session: Session = Depends(deps.get_session),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(session, db_obj=current_user, obj_in=user_in)
    session.commit()
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_session),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    session: Session = Depends(deps.get_session),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(session, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user doesn't have enough privileges")
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    session: Session = Depends(deps.get_session),
    user_id: int,
    user_in: schemas.UserUpdate,
    _: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(session, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(session, db_obj=user, obj_in=user_in)
    session.commit()
    return user


@router.delete("/{user_id}")
def delete_user(
    *,
    session: Session = Depends(deps.get_session),
    user_id: int,
    _: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    db_user = crud.user.get_by_map(session, models.User, {"id": user_id})
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user with this user id does not exist")
    session.delete(db_user)
    session.commit()
    return {"status": "success", "message": "success"}
