from mongoengine import *
from .user_model import User

DB_NAME="leyouv"

class Session:
    meta = {
        'db_alias': DB_NAME,
        'collection': 'user'
    }
    sessionid=StringField()
    user=ReferenceField(User)
    last_date=DateTimeField()
    is_active=BooleanField()

