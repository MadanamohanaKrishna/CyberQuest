from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
)


@app.get("/")
def root():
    return {
        "project": settings.app_name,
        "version": settings.version,
        "status": "development",
    }