#!/usr/bin/env python3
"""2-lifo_cache.py module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Child class of BaseCaching"""

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """and elwment to a dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last key inserted into the cache
            discarded_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item

    def get(self, key):
        """get item of a specific key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
