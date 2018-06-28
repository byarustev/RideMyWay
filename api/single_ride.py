from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sys, os

sys.path.append(os.path.pardir)
from api.modals.user import User
from api.settings.config import  rideslist,users_list,ride_requests

class SingleRide(Resource):
    """class SingleRide extends Resource class methods get
     which returns a given ride, post for creating a ride offer"""
    def get(self, ride_id):
        """returns a ride matching a given id"""

        ride = [temp_ride for temp_ride in rideslist if temp_ride["id"] == ride_id]
        if ride:
            return {"status":"success", "ride":ride, "message":"ride found"}, 200
            
        return {"status":"fail", "message":"Ride Not Found"}, 404

    def post(self):
        """creates a new ride offer"""
        parser = reqparse.RequestParser()
        parser.add_argument('origin', type=str, required=True, help="this field is required")
        parser.add_argument('destination', type=str, required=True, help="this field is required")
        parser.add_argument('dept_date', type=str, required=True, help="this field is required")
        parser.add_argument('dept_time', type=str, required=True, help="this field is required")
        parser.add_argument('slots', type=str, required=True, help="this field is required")
        parser.add_argument('description', type=str, required=True, help="this field is required")

        data = parser.parse_args()
        header_token = request.headers.get('Authorization')
        if header_token:
            user_token = header_token.split(" ")[1]
            user_id = User.decode_authentication_token(user_token)

            if isinstance(user_id, int):
                temp_ride = {"id":(len(rideslist) + 1),
                            "from":data["origin"],
                            "user_id":user_id, 
                            "to":data["destination"],
                            "dept_date":data["dept_date"],
                            "time":data["dept_time"],
                            "slots":data["slots"],
                            "description":data["description"]}
                rideslist.append(temp_ride)

                return {"status":"success","ride":temp_ride}, 201
                
        return {"status":"fail","message":"unauthorised access"}, 401 
