from config.conf import database as db_conf
import pymongo


class Database:
    _client = pymongo.MongoClient(db_conf['CONN_STRING'])
    _db = _client.get_database('bregis')
    _bsevents_collection = db_conf['bsevents_collection']
    
    @classmethod
    def get_bsevents(cls):
        return cls._db[cls._bsevents_collection].find()