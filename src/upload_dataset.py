import json

from cloudant.client import Cloudant

DATASET = "datasets/books.json"

USER = "admin"
PASSWORD = "rawpassword"
NAME = "books"
URL = "http://127.0.0.1:5984/"

client = Cloudant(USER, PASSWORD, url=URL, connect=True)
db = client[NAME]

f = open(DATASET)
for line in f.readlines():
    doc = json.loads(line)
    doc["_id"] = str(doc["_id"])
    db.create_document(doc)
f.close()
