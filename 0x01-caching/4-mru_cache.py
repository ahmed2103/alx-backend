#!/usr/bin/env python3
"""Module that represents cache system using MRU Cache policy"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class represents cache system using MRU Cache policy"""

    def __init__(self):
        """Initialize some helping types"""
        super().__init__()
        self.order = list()

    def put(self, key, item):
        """Adds item to the cache and replace another cache line according to
        MRU Cache policy"""
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                most_recent = self.order.pop()
                self.cache_data.pop(most_recent)
                print(f'DISCARD: {most_recent}')

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieves item from the cache and track the insertion order"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
