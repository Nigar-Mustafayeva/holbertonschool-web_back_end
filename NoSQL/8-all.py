#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of documents, or empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
