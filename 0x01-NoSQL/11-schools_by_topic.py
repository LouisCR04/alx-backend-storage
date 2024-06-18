#!/usr/bin/env python3
# 11-schools_by_topic.py
""" Search script """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic"""
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
