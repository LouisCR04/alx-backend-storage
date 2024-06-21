#!/usr/bin/env python3
# exercise.py
""" Redis Basic """
import redis
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4, UUID


class Cache:
    """ Implements a cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in redis & returns key
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
