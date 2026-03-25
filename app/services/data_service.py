import time
from app.core.cache import redis_client
from app.utils.logger import logger

CACHE_KEY = "heavy_data"

async def get_heavy_data():
    cached = redis_client.get(CACHE_KEY)

    if cached:
        logger.info("Cache hit")
        return {"source": "cache", "data": cached}

    logger.info("Cache miss, computing...")

    # Simulate heavy computation
    time.sleep(2)
    data = "Processed High Performance Data"

    redis_client.setex(CACHE_KEY, 60, data)

    return {"source": "computed", "data": data}
