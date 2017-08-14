import  datetime
import bson
from mongoengine import  *

DB_NAME = "leyouv"

class WX_User:
    nickName=StringField()
    avatarUrl=StringField()
    #性别    0：未知、1：男、2：女
    gender=IntField()
    province=StringField()

class User(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'user'
    }
    openid=StringField()
    name=StringField()
    birthday=DateTimeField()
    gender=IntField()
    mobile=StringField()
    followers_count=IntField()
    followings_count=IntField()
    avatar_l=StringField()
    date_added=DateTimeField()

    @property
    def user_to_dict(self):
        result={}
        for i in self:
            if isinstance(self[i],bson.objectid.ObjectId):
                result.update({i:str(self[i])})
            elif isinstance(self[i],datetime.datetime):
                result.update({i:self[i].strftime('%Y-%m-%d')})
            elif isinstance(self[i],str):
                result.update({i:str(self[i])})
            else:
                result.update({i:self[i]})
        return result