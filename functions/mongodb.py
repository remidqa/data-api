from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

mongodb_srv = os.environ.get("MONGODB_SRV")

enabled_collections = [
    "experiences",
    "faq"
]

def get_mongo_collection(coll):
    if coll not in enabled_collections:
        return f'collection "{coll}" has unauthorized access or doesn\'t exists. You must choose between : {", ".join(enabled_collections)}'
    client = MongoClient(mongodb_srv)
    db = client["data"]
    collection = db[coll]
    return collection

def find_document(coll, id):
    collection = get_mongo_collection(coll)
    document = collection.find_one({"_id": ObjectId(id)})
    return document

def all_documents(coll):
    collection = get_mongo_collection(coll)
    if coll == "experiences":
        documents = collection.find().sort([("dateStart.y", -1), ("dateStart.m",-1)])
    else:
        documents = collection.find()
    docs =[]
    for doc in documents:
        docs.append(doc)
    return docs

def insert_document(coll, document):
    collection = get_mongo_collection(coll)
    inserted_document = collection.insert_one(document)
    return inserted_document

def delete_decument(coll, id):
    collection = get_mongo_collection(coll)
    deleted_document = collection.delete_one({"_id": ObjectId(id)})
    return deleted_document

def update_document(coll, id, update):
    collection = get_mongo_collection(coll)
    updated_document = collection.update_one({"_id": ObjectId(id)}, { "$set": update})
    return updated_document