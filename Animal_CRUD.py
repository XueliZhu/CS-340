from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    def __init__(self, username, password, host, port, database):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        self.database = self.client[database]
        
        
    def create(self, document):
        try:
            self.database.animals.insert_one(document)
            return True
        except Exception as e:
            return False
        
        
    def read(self, query):
        try:
            cursor = self.database.animals.find(query)
            return list(cursor)
        except Exception as e:
            return False
        
        
    def update(self, query, updateData):
        try:
            result = self.database.animals.update_many(query, {"$set":updateData})
            return f"Modified {result.modified_count} documents"
        except Ecxception as e:
            return str(e)
        
        
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return f"Deleted {result.deleted_count} documents"
        except Exceotion as e:
            return str(e)
            