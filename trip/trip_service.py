import  json
from .trip_model import Trip
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
        print(data.count())
        for i in data:
            arr.append(i.trip_to_dict)
        return arr

    @classmethod
    def get_waypoint_list(cls):
        arr=[]
        data=Waypoint.objects[0:1]
        for i in data:
            arr.append(i.waypoint_to_dict)
        return  arr
