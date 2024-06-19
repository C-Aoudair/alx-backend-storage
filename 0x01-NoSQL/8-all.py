#!/usr/bin/env python3
""" This module contains list_all function """

import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """
    result = []
    for document in mongo_collection.find():
        result.append(document)

    return result
