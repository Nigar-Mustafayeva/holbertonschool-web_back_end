#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    nginx = db.nginx

    # Total number of logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Number of documents per HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of documents with method=GET and path=/status
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
