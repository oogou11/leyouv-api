import datetime
import  json
from .user_model import User
from trip.trip_service import Trip_Service

class User_Service:

    def __init__(self):
        pass
    
    @classmethod
    def get_user_by_id(cls,userid): 
        data=User.objects(id=userid).first() 
        user=data.user_to_dict
        trips=Trip_Service.get_trips_by_userid(userid)
        return {"user":user,"trips":trips}