#!/usr/bin/env python3
""" Main file """

import redis
get_page = __import__('web').get_page


client = redis.Redis(host='localhost', port=6379)

url = "http://slowwly.robertomurray.co.uk"

client.get(f"count:{url}")
print("hello")
print(client.get(f"count:{url}"))
get_page(url)
get_page(url)
get_page(url)
print(client.get(f"count:{url}"))
