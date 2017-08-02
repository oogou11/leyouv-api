from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult,api_wrap
from .trip_service import Trip_Service

leyouv_trips = Blueprint("leyouv_trips", __name__)

@leyouv_trips.route('/trip/index',methods=['GET'])
@api_wrap
def get_trip_list():
    data=Trip_Service.get_trip_list({})
    return APIResult(0,data)

@leyouv_trips.route('/waypoint',methods=['GET'])
@api_wrap
def get_waypoint_list():
    data=Trip_Service.get_waypoint_list()
    return  APIResult(0,data)