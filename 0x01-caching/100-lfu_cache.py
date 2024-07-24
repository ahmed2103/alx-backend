#!/usr/bin/env python3
"""Module that represents cache system using LFU Cache policy"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class represents cache system using LFU Cache policy"""

    def __init__(self):
        """Initialize some helping types"""
        super().__init__()
        self.usage_count = {}
        self.access_time = {}
        self.time_unit = 0

    def put(self, key, item):
        """Adds item to the cache and replace another cache line according to
        LFU Cache policy"""
        if key is None or item is None:
            return
        self.time_unit += 1
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_usage = min(self.usage_count.values())
                lfu_keys = (k for k, v in self.usage_count.items()
                            if v == min_usage)
                lfu_key = min(lfu_keys, key=lambda k: self.access_time[k])
                del self.usage_count[lfu_key]
                del self.access_time[lfu_key]
                del self.cache_data[lfu_key]
                print(f'DISCARD: {lfu_key}')
            self.cache_data[key] = item
            self.usage_count[key] = 1
        self.access_time[key] = self.time_unit

    def get(self, key):
        """Retrieves item from the cache and track the count and time"""
        if key in self.cache_data:
            self.time_unit += 1
            self.access_time[key] = self.time_unit
            self.usage_count[key] += 1
            return self.cache_data[key]
        return None
