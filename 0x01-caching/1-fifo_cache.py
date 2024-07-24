#!/usr/bin/env python3
"""Module that implements FIFO cache in class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Cacheing class that implements FIFO policy"""
    def __init__(self):
        """Initialize some helping types"""
        super().__init__()
        self.queue = []  # trak insertion order.

    def put(self, key, item):
        """Adds item to the dictionary cache if cache not full.
        Otherwise, discards the first"""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)   # this done to save the insertion order.
            elif len(self.cache_data) >= self.MAX_ITEMS:
                first = self.queue.pop(0)
                del self.cache_data[first]
                print(f'DISCARD: {first}')
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Retrieves key from the dictionary cache"""
        return self.cache_data.get(key, None) if key else None
