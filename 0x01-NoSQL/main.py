#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    school_collection = client.my_db['school']
    schools = list_all(school_collection)
    print(schools)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
