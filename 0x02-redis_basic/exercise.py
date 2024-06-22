#!/usr/bin/env python3
""" This module contains Cache class."""
import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method Callable argument
    and returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function for decorator"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A ecorator to store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        outputs = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", outputs)
        return outputs
    return wrapper


class Cache():
    """ Cache class that create a basic cache system"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """
        take a key string argument and an optional Callable
        argument named fn. and return the value for the key
        """
        client = self._redis
        value = client.get(key)

        if not value:
            return None

        if fn == str:
            return self.get_str(value)

        if fn == int:
            return self.get_int(value)

        if callable(fn):
            return fn(value)

        return value

    def get_str(self, value):
        """
        takes a value and return its correspondent str type
        """
        return value.decode('utf-8')

    def get_int(self, value):
        """
        takes a value and return its correspondent int type
        """
        return int(value)
