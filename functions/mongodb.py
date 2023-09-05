from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

mongodb_srv = os.environ.get("MONGODB_SRV")

def get_mongo_collection():
    client = MongoClient(mongodb_srv)
    db = client["data"]
    collection = db["faq"]
    return collection

def find_document(id):
    collection = get_mongo_collection()
    document = collection.find_one({"_id": ObjectId(id)})
    return document

def all_documents():
    collection = get_mongo_collection()
    documents = collection.find()
    docs =[]
    for doc in documents:
        docs.append(doc)
    return docs

def insert_document(document):
    collection = get_mongo_collection()
    inserted_document = collection.insert_one(document)
    return inserted_document

def delete_decument(id):
    collection = get_mongo_collection()
    deleted_document = collection.delete_one({"_id": ObjectId(id)})
    return deleted_document

def update_document(id, update):
    collection = get_mongo_collection()
    updated_document = collection.update_one({"_id": ObjectId(id)}, { "$set": update})
    return updated_document