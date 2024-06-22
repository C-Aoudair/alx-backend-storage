#!/usr/bin/env python3
""" This module contains get_page function."""

from typing import Callable
import redis
import requests
from functools import wraps

cache = redis.Redis(host="localhost", port=6379, db=0)


def cache_page(func: Callable) -> Callable:
    """decorator function"""

    @wraps(func)
    def wrapper(url: str) -> str:
        cache_key = f"page:{url}"
        count_key = f"count:{url}"

        cache.incr(count_key)

        cached_page = cache.get(cache_key)
        if cached_page:
            return cached_page.decode("utf-8")

        page_content = func(url)

        cache.setex(cache_key, 10, page_content)

        return page_content

    return wrapper


@count
def get_page(url: str) -> str:
    """
    It uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """
    return requests.get(url).text
