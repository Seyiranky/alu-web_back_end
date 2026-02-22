#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def main(collection):
    """Print statistics about nginx logs"""

    # Total number of logs
    num_logs = collection.count_documents({})
    print("{} logs".format(num_logs))

    print("Methods:")

    # List of HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count logs per method
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Count GET requests to /status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_count))


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    main(collection)
