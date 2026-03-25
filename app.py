from fastapi import FastAPI
import redis
import time

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379)

def expensive_operation():
    time.sleep(2)
    return "Heavy Data"

@app.get("/data")
def get_data():
    cached = cache.get("data")

    if cached:
        return {"source": "cache", "data": cached.decode()}

    data = expensive_operation()
    cache.set("data", data)

    return {"source": "computed", "data": data}
