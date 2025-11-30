#!/usr/bin/env python3
""" 11-schools_by_topic """

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools having a specific topic.
    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for
    Returns:
        List of school documents containing the topic
    """
    if mongo_collection is None:
        return []

    # Find documents where 'topics' array contains the given topic
    return list(mongo_collection.find({ "topics": topic }))
