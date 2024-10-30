#!/usr/bin/env python3
"""
Task 3 - Least Recently Used Cache
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class implements a Least Recently Used (LRU)
    caching strategy.
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded = self.order.pop(0)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        if key is None:
            return None
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
