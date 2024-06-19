#!/usr/bin/env python3
""" This module contains top_students function"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    for document in mongo_collection.find():
        sumOfScores = 0
        for topic in document["topics"]:
            sumOfScores += topic["score"]
        mongo_collection.update_many(
            {"name": document["name"]},
            {"$set": {"averageScore": sumOfScores / len(document["topics"])}},
        )

    return mongo_collection.find().sort("averageScore", -1)
