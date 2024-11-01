#!/usr/bin/env python3
"""
Task 2 - Last In First Out Cache

This module defines a LIFOCache class that implements a caching
strategy based on the Last In, First Out (LIFO) principle.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements a LIFO caching
    strategy, where the most recently added items are discarded first
    when the cache reaches its maximum size.

    Attributes:
        order (list): A list that maintains the order in which keys
                      are added to the cache.
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance by calling the constructor
        of the base class (BaseCaching) and initializing the order
        list to track the order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache using the LIFO strategy.

        Args:
            key: The key under which the item will be stored.
            item: The item to be cached.

        If either key or item is None, the method returns immediately.
        Otherwise, the item is stored in the cache data dictionary.
        If the key is not already in the order list, it is appended.
        If the number of cached items exceeds MAX_ITEMS, the most
        recently added item is discarded from both the cache and
        the order list, and a discard message is printed.
        """
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
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item associated with the key, or None if the
            key is None or not found in the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
