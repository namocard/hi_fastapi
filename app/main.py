from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings

app = FastAPI(title="Hi FastAPI", openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router)
