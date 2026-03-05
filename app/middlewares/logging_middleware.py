import time
import logging
from fastapi import Request


logger = logging.getLogger("request_logger")


async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
    f"{request.method} {request.url.path} " 
    f"Status: {response.status_code} " 
    f"Time: {process_time}ms"
    )

    return response