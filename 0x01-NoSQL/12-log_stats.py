#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
import pymongo

def nginx_log_stats(db_name, collection_name):
  """
  Provides stats about Nginx logs stored in MongoDB.

  Args:
    db_name: The name of the database.
    collection_name: The name of the collection.
  """

  client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your connection string
  db = client[db_name]
  collection = db[collection_name]

  # Total logs
  total_logs = collection.count_documents({})
  print(f"{total_logs} logs")

  # Methods
  print("Methods:")
  methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
  for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\t{method}: {count}")

  # GET /status
  get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
  print(f"\tGET /status: {get_status_count}")

if __name__ == "__main__":
  nginx_log_stats("logs", "nginx")

