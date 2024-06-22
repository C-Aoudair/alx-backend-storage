#!/usr/bin/env python3
""" This module contains get_page function."""

from functools import wraps
from typing import Callable
import redis
import requests


def count(func: Callable) -> Callable:
    """
    function decorator that count how many times a given url
    was accessed.
    """
    @wraps(func)
    def inner(url: str) -> str:
        client = redis.Redis(host='localhost', port=6379)
        client.incr(f"count:{url}")
        if client.get(f"{url}"):
            return client.get(f"{url}").decode('utf-8')
        response = func(url)
        client.set(f"{url}", response, 10)
        return response

    return inner


@count
def get_page(url: str) -> str:
    """
    It uses the requests module to obtain the HTML content
    of a particular URL and returns it.
    """
    return requests.get(url).text
