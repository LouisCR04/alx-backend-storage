#!/usr/bin/env python3
# 8-all.py
"""
Pymongo ODM
"""


def list_all(mongo_collection):
    """ Lists all docs in mongo collection """
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs
