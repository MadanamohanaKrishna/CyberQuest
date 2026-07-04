from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/")
def root():
    return {
        "project": settings.app_name,
        "version": settings.version,
        "status": "development",
    }