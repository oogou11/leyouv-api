import  json
from .trip_model import Trip
from .day_model import Days
from .waypoint_model import Waypoint

class Trip_Service:

    def __init__(self):
        pass

    @classmethod
    def get_trip_list(cls):
        arr=[]
        offset=0,
        num=5
        data=Trip.objects.order_by('-id').skip(0).limit(5)
        for i in data:
            arr.append(i.trip_to_dict)
        result={"data":arr}
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
            print(i.id)
            day={}
            waypoints=cls._get_waypoits_by_days_id(i.id)
            day.update({"day":i.day,"date":i.date_add,"waypoints":waypoints})
            arr.append(day)
        return arr

    @classmethod
    def get_waypoint_list(cls):
        arr=[]
        data=Waypoint.objects[0:1]
        for i in data:
            arr.append(i.waypoint_to_dict)
        return  arr

    def _get_waypoits_by_days_id(self,daysid):
        result=[]
        waypoints=Waypoint.objects(day=daysid).order_by('id')
        for i in waypoints:
            result.append(i.waypoint_to_dict)
        return  result