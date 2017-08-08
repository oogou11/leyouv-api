import  datetime
import bson
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


    @property
    def user_to_dict(self):
        result={}
        for i in self:
            if isinstance(self[i],bson.objectid.ObjectId):
                result.update({i,str(self[i])})
            elif isinstance(self[i],datetime):
                result.update({i,self[i].strftime('%Y-%m-%d')})
            else:
                result.update({i: self[i]})
        return result