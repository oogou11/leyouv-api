import  datetime
import bson
from mongoengine import *
from .waypoint_model import Waypoint

DB_NAME = "leyouv"

class Trip(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'trip'
    }
    name=StringField(max_length=100)
    user_id=ObjectIdField()
    person_num=IntField()
    share_count=IntField()
    day_count=IntField()
    cover_image_default=StringField()
    first_day=DateTimeField()
    last_day=DateTimeField()
    view_count=IntField()
    liked_count=IntField()
    comment_count=IntField()
    date_added=DateTimeField(default=datetime.datetime.now)


    @property
    def trip_to_dict(self):
        data={}
        for i in self:
            if isinstance(self[i],datetime.datetime):
                data.update({i:self[i].strftime('%Y-%m-%d')})
            elif isinstance(self[i],bson.objectid.ObjectId):
                data.update({i:str(self[i])})
            else:
                data.update({i: self[i]})
        return data