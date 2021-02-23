from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str


class AdminUserCreate(UserCreate):
    secret_key: str


class UserUpdate(UserBase):
    password: Optional[str]


class UserDbBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserDbBase):
    pass
