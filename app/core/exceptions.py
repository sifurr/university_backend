from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError


def error_response(message: str, status_code: int):
    """
    Standard API error response format
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message            
        }
    )

async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
):
    return error_response("validation error", 422)

async def integrity_exception_handler(
        request: Request,
        exc: IntegrityError
):
    return error_response("Database intregrity violation", 400)

