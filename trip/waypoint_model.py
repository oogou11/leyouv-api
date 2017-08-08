import datetime
import bson
import json
from mongoengine.base.datastructures import BaseList
from mongoengine import *
from user.user_model import User
from .day_model import Days


DB_NAME = "leyouv"


class Recommenders(EmbeddedDocument):
    date_added = DateTimeField()
    user = ObjectIdField()


class Commnets(EmbeddedDocument):
    comment = StringField()
    date_added = DateTimeField()
    user = ObjectIdField()


class Waypoint(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'waypoint'
    }
    local_time = DateTimeField()
    customer_id = IntField
    photo = StringField()
    fee = StringField()
    text = StringField()
    hotel = StringField()
    comment_count = IntField()
    recommender_count = IntField()
    comments = ListField(EmbeddedDocumentField(Commnets))
    recommenders = ListField(EmbeddedDocumentField(Recommenders))
    days = ReferenceField(Days)

    @property
    def waypoint_to_dict(self):
        data = {}
        for i in self:
            if isinstance(self[i], datetime.datetime):
                data.update({i: self[i].strftime('%Y-%m-%d %H:%M:%S')})
            elif isinstance(self[i], bson.objectid.ObjectId):
                data.update({i: str(self[i])})
            elif isinstance(self[i], BaseList):
                arr = []
                for j in self[i]:
                    arr.append(self._for_model_key(j))
                data.update({i: arr})

            elif isinstance(self[i], str):
                data.update({i: str(self[i])})
            elif isinstance(self[i], Days):
                data['day'] = self[i].day
            else:
                data.update({i: self[i]})
        return data

    def _for_model_key(self, model):
        data = {}
        for i in model:
            if isinstance(model[i], datetime.datetime):
                data.update({i: model[i].strftime('%Y-%m-%d')})
            elif isinstance(model[i], bson.objectid.ObjectId):
                user_info = User.objects(id=model[i]).first()
                user = {
                    "id": str(user_info.id),
                    "name": (user_info.name),
                    "avatar_1": user_info.avatar_1
                }
                data['user'] = user
            elif isinstance(model[i], str):
                data.update({i: str(model[i])})
            else:
                data.update({i: model[i]})
        return data
