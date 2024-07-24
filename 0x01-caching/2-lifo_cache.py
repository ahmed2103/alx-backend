#!/usr/bin/env python3
"""Module represents LIFO cache Class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Cache class that implements LIFO replacement policy"""
    def __init__(self):
        """Initialize some helping types"""
        super().__init__()
        self.stack = list()

    def put(self, key, item):
        """Add items to the dictionary cache and handles
            the capacity if over"""
        if key and item:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last = self.stack.pop()
                del self.cache_data[last]
                print(f'DISCARD: {last}')
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """Retrieve item from the dictionary cache if it exists.
            Otherwise, return None"""
        return self.cache_data.get(key, None) if key else None
