from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logging_config import setup_logging
import logging
from app.middlewares.logging_middleware import log_requests

from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.core.exceptions import (
    validation_exception_handler, integrity_exception_handler
)
from app.core.exceptions import (
    BadRequestException,
    bad_request_exception_handler
)

from app.api.v1.api import router as api_router

from app.middlewares.monitoring_middleware import monitoring_middleware
from app.api.metrics import router as metrics_router


setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

logger.info("Application started successfully")

app.middleware("http")(log_requests)
app.middleware("http")(monitoring_middleware)

# CORS 
# origins = [
#     "http://localhost:5173",  # আপনার Vite ফ্রন্টএন্ডের ইউআরএল
#     "http://127.0.0.1:5173",
# ]

# always add to the last
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],                           # কোন কোন ইউআরএল থেকে রিকোয়েস্ট আসবে
    allow_credentials=True,
    allow_methods=["*"],              # GET, POST, PUT, DELETE সব এলাউ করবে
    allow_headers=["*"],              # সব ধরনের হেডার এলাউ করবে
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

app.add_exception_handler(
    BadRequestException,
    bad_request_exception_handler
)


@app.get("/health")
def health_check():
    """
    Used by monitoring tools.
    """
    return {
        "status": "ok", 
        "service": "university-backend"
    }

# Include API routers
app.include_router(api_router)
app.include_router(metrics_router)

