#!/usr/bin/env python3
"""
Task 100 - Least Frequently Used Cache

This module defines an LFUCache class that implements a caching
strategy based on the Least Frequently Used (LFU) principle.
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements an LFU caching
    strategy, where the least frequently accessed items are discarded
    first when the cache reaches its maximum size.

    Attributes:
        freq (defaultdict): A dictionary that maps keys to their
                            access frequencies.
        order (list): A list that maintains the order of keys
                      based on their insertion order.
    """

    def __init__(self):
        """
        Initializes the LFUCache instance by calling the constructor
        of the base class (BaseCaching) and initializing the frequency
        dictionary and order list to track the keys.
        """
        super().__init__()
        self.freq = defaultdict(int)  # Frequency of each key
        self.order = []  # Order of keys

    def put(self, key, item):
        """
        Adds an item to the cache using the LFU strategy.

        Args:
            key: The key under which the item will be stored.
            item: The item to be cached.

        If either key or item is None, the method returns immediately.
        If the key already exists in the cache, its frequency is
        incremented and the item is updated. If the cache is full
        (i.e., the number of cached items is equal to or exceeds
        MAX_ITEMS), the least frequently used item is discarded.
        In case of a tie, the first key found in insertion order is
        discarded. Finally, the new item is added to the cache with
        an initial frequency of 1.
        """
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
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item associated with the key, or None if the
            key is None or not found in the cache. If the key is found,
            its frequency is incremented.
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        return self.cache_data[key]
