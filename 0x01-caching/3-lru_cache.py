#!/usr/bin/env python3
"""
Task 3 - Least Recently Used Cache

This module defines an LRUCache class that implements a caching
strategy based on the Least Recently Used (LRU) principle.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and implements a LRU caching
    strategy, where the least recently accessed items are discarded
    first when the cache reaches its maximum size.

    Attributes:
        order (list): A list that maintains the order of keys based
                      on their access times, with the least recently
                      used items at the front.
    """

    def __init__(self):
        """
        Initializes the LRUCache instance by calling the constructor
        of the base class (BaseCaching) and initializing the order
        list to track the order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache using the LRU strategy.

        Args:
            key: The key under which the item will be stored.
            item: The item to be cached.

        If either key or item is None, the method returns immediately.
        If the key already exists in the cache, it is removed from the
        order list to update its access time. If the cache is full
        (i.e., the number of cached items is equal to or exceeds
        MAX_ITEMS), the least recently used item (the first item in
        the order list) is discarded from both the cache and the order
        list, and a discard message is printed. Finally, the new item
        is added to the cache and the order list.
        """
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
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item associated with the key, or None if the
            key is None or not found in the cache. If the key is found,
            it is moved to the end of the order list to mark it as
            recently used.
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
