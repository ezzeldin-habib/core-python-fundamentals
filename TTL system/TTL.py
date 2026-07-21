import time
class TTLCache:
    def __init__(self):
        self.storage = {}
    def set(self, key, value, ttl):
        expiry_time = time.time() + ttl
        self.storage[key] = (value, expiry_time)
    def get(self, key):
        result = self.storage.get(key)
        if result is None:
            return None
        value, expiry_time = result
        if time.time() > expiry_time:
            return None
        return value



cache = TTLCache()
cache.set("username", "Ahmed", 2 )
print(cache.get("username"))
time.sleep(3)
print(cache.get("username"))



