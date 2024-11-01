#!/usr/bin/env python3
"""
Task 0 - Basic Cache

This module defines a BasicCache class that implements
a simple caching mechanism without any limits on the
number of items that can be stored.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and provides a caching system
    that allows items to be added without restriction.

    Attributes:
        cache_data (dict): A dictionary that stores cached items.
    """

    def __init__(self):
        """
        Initializes the BasicCache instance by calling the constructor
        of the base class (BaseCaching) to set up the cache data structure.
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be cached.

        If either key or item is None, the method does nothing. Otherwise,
        it stores the item in the cache data dictionary using the provided key.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The cached item associated with the key, or None if the key is
            None or not found in the cache.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
