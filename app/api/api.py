from fastapi import APIRouter

from app.core.config import settings
from app.api.v1.api import v1_api_router

api_router = APIRouter()

api_router.include_router(v1_api_router, prefix=settings.API_V1_STR)
