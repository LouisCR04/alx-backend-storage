#!/usr/bin/env python3
# 9-insert_school.py
""" Pymongo ops """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new doc in a collection based on kwargs """
    return mongo_collection.insert(kwargs)
