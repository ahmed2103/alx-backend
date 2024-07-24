#!/usr/bin/env python3
"""Module that implements LRU Cache policy"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that implements LRU Cache policy"""

    def __init__(self):
        """Initialize some helping types"""
        super().__init__()
        self.order = list()  # Here we track both order of insertion & usage.

    def put(self, key, item):
        """Adds item to the cache if not full
            Otherwise, removes according to LRU Cache policy"""
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)  # to track insertion order.
            elif len(self.cache_data) >= self.MAX_ITEMS:
                least_recent = self.order.pop(0)
                self.cache_data.pop(least_recent)
                print(f'DISCARD: {least_recent}')

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """get the key if present in the cache.
            Otherwise, Null and track the usage order"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
