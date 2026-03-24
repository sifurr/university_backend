import redis 

redis_client = relis.Redis(
    host = "redis", # docker service
    port = 6379
    db=0
    decode_responses = True
)