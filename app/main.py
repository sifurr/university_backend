from app.core.logging_config import setup_logging
import logging
from app.middlewares.logging_middleware import log_requests

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.core.exceptions import (
    validation_exception_handler, integrity_exception_handler
)

from app.api.v1.api import router as api_router

from app.middlewares.monitoring_middleware import monitoring_middleware
from app.api.metrices import router as metrics_router


setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

logger.info("Application started successfully")

app.middleware("http")(log_requests)
app.middleware("http")(monitoring_middleware)




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
    return {
        "status": "ok", 
        "service": "university-backend"
    }

# Include API routers
app.include_router(api_router)
app.include_router(metrics_router)

