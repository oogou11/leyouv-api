from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap
from .trip_service import Trip_Service
import logging

leyouv_trips = Blueprint("leyouv_trips", __name__)
logger = logging.getLogger('trips')


@leyouv_trips.route('/trips/index', methods=['GET'])
@api_wrap
def get_trip_list():
    try:
        next_start = request.args.get('next_start')
        if next_start:
            next_start = int(next_start)
        else:
            next_start = 0
        data = Trip_Service.get_trip_list(next_start)
        return APIResult(0, data)
    except Exception as ex:
        logger.error('get_trip_list error:>> %s', ex)
        return APIResult(201, 'error')


@leyouv_trips.route('/trip/<tripid>', methods=['GET'])
@api_wrap
def get_trip_by_id(tripid):
    try:
        data = Trip_Service.get_trip_by_id(tripid)
        return APIResult(0, data)
    except Exception as ex:
        logger.error('get_trip_by_id error:>> %s', ex)
        return APIResult(201, 'error')


@leyouv_trips.route('/trip/<tripid>/waypoints', methods=['GET'])
@api_wrap
def get_waypoint_list(tripid):
    try:
        # get trips
        trip = Trip_Service.get_trip_by_id(tripid)
        days = Trip_Service.get_days_by_tripsid(tripid)
        data = {"trip": trip, "days": days}
        return APIResult(0, data)
    except Exception as ex:
        logger.error('get_waypoint_list error:>> %s', ex)
        return APIResult(201, 'error')


@leyouv_trips.route('/waypoint/detail/<waypointId>', methods=['GET'])
@api_wrap
def get_detail_waypoint(waypointId):
    try:
        # get detail waypoints
        data = Trip_Service.get_detail_waypoint(waypointId)
        return APIResult(0, data)
    except Exception as ex:
        logger.error('get_detail_waypoint error:>>%s ', ex)
        return APIResult(201, 'error')
