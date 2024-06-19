#!/usr/bin/env python3
"""
This Module contains script that provides some stats about Nginx
logs stored in MongoDB.
"""

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print(f"{logs.count_documents({})} logs")
    print("Methods:")
    for method in methods:
        count = logs.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    
    statsCount = logs.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{statsCount} status check")
