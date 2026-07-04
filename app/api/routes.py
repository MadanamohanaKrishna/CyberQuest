from fastapi import APIRouter
from app.core.config import settings
from app.core.exceptions import AppException

router = APIRouter()

@router.get("/")
def root():
    return {
        "project": settings.app_name,
        "version": settings.version,
        "status": "development",
    }

@router.get("/health")
def health_check():
    return  {"status": "healthy"}