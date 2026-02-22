#!/usr/bin/env python3
'''Python module to list collection docs.
'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]