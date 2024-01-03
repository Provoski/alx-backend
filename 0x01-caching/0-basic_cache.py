#!/usr/bin/env python3
"""0-basic_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Child class of BaseCaching"""

    def put(self, key, item):
        """assigh items to a dictionary"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value of a particular dictionary key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
