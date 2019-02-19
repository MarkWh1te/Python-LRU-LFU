"""Python Implementation of Least recently used (LRU)
https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
"""
from collections import deque
from typing import Any, Hashable


class LRU_Cache(object):
    """
    Least recently used (LRU) cache
    """

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__map = dict()
        self.__dll = deque()

    def set(self, key: Hashable, value: Any):
        if key in self.__dll:
            self.__dll.remove(key)
            self.__dll.appendleft(key)
        else:
            if len(self.__dll) < self.__capacity:
                self.__dll.appendleft(key)
            # reached the capacity
            else:
                remove_key = self.__dll.pop()
                # delete key in map
                del self.__map[remove_key]
                self.__dll.appendleft(key)

        # always set key in map
        self.__map[key] = value

    def get(self, key) -> Any:
        if key in self.__dll:
            self.__dll.remove(key)
            self.__dll.appendleft(key)
            return self.__map[key]
        else:
            return -1