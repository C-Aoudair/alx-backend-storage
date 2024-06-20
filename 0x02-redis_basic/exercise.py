#!/usr/bin/env python3
""" This module contains Cache class."""
import redis
import uuid
from typing import Any


class Cache():
    """ Cache class that create a basic cache system"""
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data: Any) -> str:
        """ takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
