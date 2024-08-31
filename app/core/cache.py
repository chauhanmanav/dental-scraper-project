import redis

class Cache:
    def __init__(self):
        self.r = redis.Redis()

    def is_cached(self, product_title: str, product_price: float) -> bool:
        cached_price = self.r.get(product_title)
        return cached_price is not None and float(cached_price) == product_price

    def update_cache(self, product_title: str, product_price: float):
        self.r.set(product_title, product_price)
