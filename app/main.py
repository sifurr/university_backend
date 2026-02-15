from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.core.exceptions import (
    validation_exception_handler, integrity_exception_handler
)

from app.api.v1.api import router as user_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

# Register exception handlers
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    IntegrityError,
    integrity_exception_handler
)


@app.get("/health")
def health_check():
    """
    Used by monitorintg tools.
    """
    return {"status": "ok"}

# Include API routers
app.include_router(user_router)

