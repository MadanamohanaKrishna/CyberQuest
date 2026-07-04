from fastapi import Request, status
from fastapi.responses import JSONResponse

class AppException(Exception):
    pass

async def app_exception_handler(
    request: Request,
     exc: AppException,
):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )