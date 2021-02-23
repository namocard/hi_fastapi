from fastapi import APIRouter

from app.api.v1.endpoints import grades, login, schools, users

v1_api_router = APIRouter()
v1_api_router.include_router(grades.router, prefix="/grades", tags=["grades"])
v1_api_router.include_router(schools.router, prefix="/schools", tags=["schools"])
v1_api_router.include_router(login.router, tags=["login"])
v1_api_router.include_router(users.router, prefix="/users", tags=["users"])
