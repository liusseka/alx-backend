#!/usr/bin/env python3
"""
Task 100 - Least Frequently Used Cache
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    This class implements a Least Frequently Used (LFU)
    caching strategy.
    """
    def __init__(self):
        super().__init__()
        self.freq = defaultdict(int)
        self.order = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.freq[key] += 1
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.freq.values())
            lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
            lru_key = lfu_keys[0]
            del self.cache_data[lru_key]
            del self.freq[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.freq[key] = 1
        self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        return self.cache_data[key]
