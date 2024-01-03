#!/usr/bin/env python3
"""100-lfu_cache.py module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """child class"""

    def __init__(self):
        """init method"""

        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """insert item into a dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """Find the least frequency used key(s)"""
            min_frequency = min(self.frequency.values())
            least_frequent_keys = [
                    k for k, v in self.frequency.items() if v == min_frequency]
            if len(least_frequent_keys) > 1:
                """Use LRU algorithm to break ties"""
                discarded_key = self._find_lru_key(least_frequent_keys)
            else:
                discarded_key = least_frequent_keys[0]

            del self.cache_data[discarded_key]
            del self.frequency[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """retrieve item from a dictionary"""
        if key is None or key not in self.cache_data:
            return None

        """Increment the frequency for the accessed key"""
        self.frequency[key] += 1

        return self.cache_data[key]

    def _find_lru_key(self, keys):
        """Find the least recently used key among the given keys
        """
        return min(keys, key=lambda k: self.frequency[k])
