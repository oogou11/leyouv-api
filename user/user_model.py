from mongoengine import  *

DB_NAME = "leyouv"

class User(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'user'
    }

    name=StringField()
    birthday=DateTimeField()
    gender=IntField()
    mobile=StringField()
    followers_count=IntField()
    followings_count=IntField()
    avatar_1=StringField()
    date_added=DateTimeField()