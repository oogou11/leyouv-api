import datetime
import  json
from .trip_model import Trip
from .day_model import Days
from .waypoint_model import Waypoint

class Trip_Service:

    def __init__(self):
        pass

    @classmethod
    def get_trip_list(cls,next_start):
        arr=[] 
        num=5
        data=Trip.objects.order_by('-id').skip(next_start).limit(5)
        if len(data)==0:
            return {"data":arr,"next_start":next_start}
        for i in data:
            arr.append(i.trip_to_dict)
        result={"data":arr,"next_start":next_start+num}
        return result

    @classmethod
    def get_trip_by_id(cls,id):
        data=Trip.objects(id=id).first()
        result=data.trip_to_dict
        return  result

    @classmethod
    def get_days_by_tripsid(cls,tripsid):
        arr=[]
        days_info=Days.objects(trip=tripsid)
        for i in days_info:
            day={}
            waypoints=cls._get_waypoits_by_days_id(i.id)
            day.update({"day":i.day,"date":i.date_add.strftime('%Y-%m-%d'),"waypoints":waypoints})
            arr.append(day)
        return arr

    @classmethod
    def get_waypoint_list(cls):
        arr=[]
        data=Waypoint.objects[0:1]
        for i in data:
            arr.append(i.waypoint_to_dict)
        return  arr
    
    @classmethod
    def get_detail_waypoint(cls,waypointId): 
        waypoint_detail=Waypoint.objects(id=waypointId).first()
        reuslt=waypoint_detail.waypoint_to_dict
        return reuslt

    @classmethod
    def get_trips_by_userid(cls,userid):
        arr=[]
        data=Trip.objects(user=userid)
        for i in data:
            arr.append(i.trip_to_dict)
        return arr

    def _get_waypoits_by_days_id(daysid): 
        print(daysid)
        result=[]
        waypoints=Waypoint.objects(days=daysid).order_by('id')
        for i in waypoints:
            result.append(i.waypoint_to_dict)
        return  result