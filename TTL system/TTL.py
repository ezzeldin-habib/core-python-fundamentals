import time


class TTLCache:
    """
    An in-memory data store with Time-To-Live (TTL) eviction logic.
    Maintains temporary key-value schemas mimicking high-speed Redis database storage systems.
    """

    def __init__(self):
        """
        Initializes an empty state repository dictionary to map cache entries.
        """
        self.storage = {}

    def set(self, key, value, ttl):
        """
        Stores an item in the cache payload linked to a future timestamp ceiling.

        Args:
            key (str): The unique identifier lookup token.
            value (any): The data record payload to preserve in memory.
            ttl (int/float): Lifespan duration metric in seconds.
        """
        # Calculate absolute Unix epoch expiration boundary
        expiry_time = time.time() + ttl
        self.storage[key] = (value, expiry_time)

    def get(self, key):
        """
        Retrieves a cache item after performing validation checks against its expiration window.
        Lazily evicts records if the systemic operational time crosses the calculated ceiling.

        Args:
            key (str): The target identifier lookup token.
        Returns:
            any/None: The preserved value if valid; None if missing or expired.
        """
        result = self.storage.get(key)
        if result is None:
            return None

        value, expiry_time = result
        # Structural check to validate data expiration state
        if time.time() > expiry_time:
            return None
        return value


# Execution routine simulating temporary session management pipelines
cache = TTLCache()
cache.set("username", "Ahmed", 2)

# Operational check: Retrieve active in-memory token
print(cache.get("username"))

# Introduce execution delay to trigger threshold eviction boundary
time.sleep(3)

# Operational check: Token should be expired and return None
print(cache.get("username"))
