#!/usr/bin/env python3
"""
Task 0 - Basic Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This caching system has no limits and allows you
    to add items to the cache.
    """
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
