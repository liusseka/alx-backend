#!/usr/bin/env python3
"""
Task 2 - Last in First Out Cache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class implements a LIFO (Last In, First Out)
    caching strategy.
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded = self.order.pop()
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key, None)
