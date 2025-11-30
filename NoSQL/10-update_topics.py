#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of a school document based on its name.
    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of topics to set
    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },           # filter by school name
        { "$set": { "topics": topics } }  # set/update the topics field
    )
