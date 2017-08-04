import datetime
import bson
import json
from mongoengine.base.datastructures import BaseList
from mongoengine import *
from user.user_model import User


DB_NAME = "leyouv"

class CommentUser(EmbeddedDocument):
    user = ReferenceField(User)

class Commnets(EmbeddedDocument):
    user=EmbeddedDocumentField(CommentUser)
    comment=StringField()
    date_added=DateTimeField()


class Waypoint(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'waypoint'
    }
    trip_id=ObjectIdField()
    day=IntField()
    local_time=DateTimeField()
    customer_id = IntField
    photo = StringField()
    fee = StringField()
    text = StringField()
    hotel = StringField()
    comment_count = IntField()
    recommender_count = IntField()
    comment = ListField(EmbeddedDocumentField(Commnets))

    @property
    def waypoint_to_dict(self):
        data = {}
        for i in self:
            if isinstance(self[i], datetime.datetime):
                data.update({i: self[i].strftime('%Y-%m-%d')})
            elif isinstance(self[i], bson.objectid.ObjectId):
                data.update({i: str(self[i])})
            elif isinstance(self[i],BaseList):
                print(i,self[i])
                comments=[]
                for j in self[i]:
                    comments.append(self._for_model_key(j))
                print(comments)
                data.update({i:comments})
            else:
                data.update({i: self[i]})
        return data


    def _for_model_key(self,model):
        data={}
        for i in model:
            if isinstance(model[i], datetime.datetime):
                data.update({i: model[i].strftime('%Y-%m-%d')})
            elif isinstance(model[i], bson.objectid.ObjectId):
                data.update({i: str(model[i])})
            elif isinstance(model[i],User):
                user = {
                    "id": str(self[i].id),
                    "name": (self[i].name),
                    "avatar_1": self[i].avatar_1
                }
                data['user'] = user
            else:
                data.update({i: model[i]})
        return  data






