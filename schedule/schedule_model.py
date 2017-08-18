from mongoengine import *

DB_NAME = "leyouv"

class Days(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'schedule'
    }


