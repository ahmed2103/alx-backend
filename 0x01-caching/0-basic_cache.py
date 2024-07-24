#!/usr/bin/env python3
"""Module contains caching class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching class that is subclass of BaseCaching"""
    def put(self, key, item):
        """Store item into cache by key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache by key if exists"""
        return self.cache_data.get(key, None) if key else None
