from os import name

from pymongo.database import Database
from pymongo.server_selectors import Selection
from utils.ConfigReader import ConfigReader
from pymongo import MongoClient
from urllib.parse import quote_plus

class PyMongoConnection():
    instance = None
    _database: Database

    def __init__(self):
        if PyMongoConnection.instance is not None:
            raise Exception('Use getInstance')
        PyMongoConnection.instance = self
    
    def get_database(self):
        return self._database

    def get_collection(self, name=''):
        return self._database.get_collection(name)

    @staticmethod
    def create(config_reader: ConfigReader):
        if PyMongoConnection.instance is not None:
            return PyMongoConnection.instance
        config = config_reader.get_dict_by_section('DATABASE')
        host = config['host']
        connection = host.replace('<password>', config['password'])
        mongo_client = MongoClient(host=connection)
        PyMongoConnection.instance = PyMongoConnection()
        PyMongoConnection._database = mongo_client.get_default_database()
        return PyMongoConnection.instance