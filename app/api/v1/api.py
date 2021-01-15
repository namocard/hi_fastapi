from fastapi import APIRouter

from app.api.v1.endpoints import schools

v1_api_router = APIRouter()
v1_api_router.include_router(schools.router, prefix="/schools", tags=["schools"])
# api_router.include_router(login.router, tags=["login"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
