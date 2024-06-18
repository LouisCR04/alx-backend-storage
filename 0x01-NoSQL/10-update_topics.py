#!/usr/bin/env python3
# 10-update_topics.py

""" Change school topics """


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school doc based on name"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
