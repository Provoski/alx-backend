#!/usr/bin/env python3
"""2-lifo_cache.py module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """child class"""

    def __init__(self):
        """init method"""

        super().__init__()
        self.order = []

    def put(self, key, item):
        """insert itwm into a dictionary"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """Get the most recently used key
            (last in the order list)
            """
            discarded_key = self.order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """get element of a specific key"""
        if key is None or key not in self.cache_data:
            return None

        """Move the accessed key to the end of the order
        list (most recently used)
        """
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
