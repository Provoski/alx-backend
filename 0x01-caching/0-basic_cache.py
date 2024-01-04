#!/usr/bin/env python3
"""0-basic_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Child class of BaseCaching"""

    def put(self, key, item):
        """insert item into a dictionary"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """get itwm from a dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
