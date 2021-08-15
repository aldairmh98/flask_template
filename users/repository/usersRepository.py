from bson.objectid import ObjectId
from utils.ConfigReader import ConfigReader
from pymongo import collection
from utils.PyMongoConnection import PyMongoConnection
class UserRepository:

    _collection: collection.Collection

    def __init__(self, config_reader: ConfigReader) -> None:
        self._collection = PyMongoConnection.create(config_reader).get_collection('users')

    def create(self,name):
        self._collection.insert_one({'name': name})
    
    def find_all(self):
        return self._collection.find()

    def remove(self,id):
        return self._collection.remove({'_id': ObjectId(id)})