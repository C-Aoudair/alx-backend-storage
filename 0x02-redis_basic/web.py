#!/usr/bin/env python3
""" This module contains get_page function."""

import redis
import requests
from functools import wraps
from typing import Callable


cache = redis.Redis(host='localhost', port= 6379)
"""
The module-level Redis instance.
"""


def count(func: Callable) -> Callable:
    """
    Caches the output of fetched data.
    """
    @wraps(func)
    def wrapper(url) -> str:
        """
        The wrapper function for caching the output.
        """
        cache.incr(f'count:{url}')
        result = cache.get(f'{url}')
        if result:
            return result.decode('utf-8')
        result = func(url)
        cache.setex(f'{url}', 10, result)
        return result
    return wrapper


@count
def get_page(url: str) -> str:
    """
    Returns the content of a URL after caching the request's
    response, and tracking the request.
    """
    return requests.get(url).text
