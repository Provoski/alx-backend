#!/usr/bin/env python3
"""3-lru_cache.py module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """child clasw of BaseCaching"""

    def __init__(self):
        """init module"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add item to a dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """Get the least recently used key
            (first in the order list)
            """
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """get item of a specific key"""
        if key is None or key not in self.cache_data:
            return None

        """Move the accessed key to the end of the
        order list (most recently used)
        """
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
