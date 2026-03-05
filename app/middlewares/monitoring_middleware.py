import time
from fastapi import Request
from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY


async def monitoring_middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time =  time.time() - start_time
    endpoint = request.url.path

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(endpoint=endpoint).observe(process_time)

    return response