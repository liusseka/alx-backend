#!/usr/bin/python3
"""
Task 0 - Basic Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This caching system has no limits and allows you
    to add items to the cache.
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key, None)
