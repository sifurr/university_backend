from prometheus_client import Counter, Histogram


# Total API requests counter
REQUEST_COUNT = Counter(
   "api_requests_total",
   "Total number of API requests",
   ["method", "endpoint", "status"] 
)

# Request latency
REQUEST_LATENCY = Histogram(
    "api_request_laten_seconds",
    "API request latency",
    ["endpoint"]
)

# Error counter
ERROR_COUNT = Counter(
    "api_errors_total",
    "Total number of API errors",
    ["endpoint"]
)


