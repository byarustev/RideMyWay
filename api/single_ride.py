from api.modals.user import User
from api.modals.ride import Ride
from api.settings.config import rideslist
from flask import request
from flask_restful import Resource, reqparse
import sys
import os
sys.path.append(os.path.pardir)


class SingleRide(Resource):
    """class SingleRide extends Resource class methods get
     which returns a given ride, post for creating a ride offer"""
    def get(self, ride_id):
        """returns a ride matching a given id"""

        ride = [temp_ride for temp_ride in rideslist if temp_ride["id"] == ride_id]
        if ride:
            return {"status": "success", "ride": ride, "message": "ride found"}, 200
            
        return {"status": "fail", "message": "Ride Not Found"}, 404

    def post(self):
        """creates a new ride offer"""
        parser = reqparse.RequestParser()
        parser.add_argument('origin', type=str, required=True, help="origin field is required")
        parser.add_argument('destination', type=str, required=True, help="destination field is required")
        parser.add_argument('departure_time', type=str, required=True, help="departure_time field is required")
        parser.add_argument('slots', type=str, required=True, help="slots field is required")
        parser.add_argument('description', type=str, required=True, help="description field is required")

        data = parser.parse_args()
        header_token = request.headers.get('Authorization')
        if header_token:
            user_token = header_token.split(" ")[1]
            user_id = User.decode_authentication_token(user_token)

            if isinstance(user_id, int):
                temp_ride = Ride(None, user_id, data["origin"], data["destination"], data["departure_time"], data["slots"], data["description"])

                Ride.create_ride(temp_ride)
                return {"status": "success", "ride": temp_ride.__dict__}, 201
                
        return {"status": "fail", "message": "unauthorised access"}, 401
