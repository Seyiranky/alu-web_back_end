#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            collection.count_documents({"method": method})
        ))

    print("{} status check".format(
        collection.count_documents({"method": "GET", "path": "/status"})
    ))
