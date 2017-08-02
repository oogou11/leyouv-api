import datetime
import bson
from mongoengine import *


DB_NAME = "leyouv"

class Commnets(EmbeddedDocument):
    user_id=ObjectIdField()
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
            print(i,type(i))
            if isinstance(self[i], datetime.datetime):
                data.update({i: self[i].strftime('%Y-%m-%d')})
            elif isinstance(self[i], bson.objectid.ObjectId):
                data.update({i: str(self[i])})
            elif i=='comment':
                continue
            else:
                data.update({i: self[i]})
        return data






