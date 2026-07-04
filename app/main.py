from fastapi import FastAPI
from app.core.config import settings
from contextlib import asynccontextmanager
from app.core.logger import logger
from app.api.routes import router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("CyberQuest API started")
    yield
    logger.info("CyberQuest API shutting down")

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    lifespan=lifespan
)

app.include_router(router)
