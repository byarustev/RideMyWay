from api.modals.user import User
from api.settings.config import ride_requests, rideslist
from flask import request
from flask_restful import Resource
import sys
import os
sys.path.append(os.path.pardir)


class MyTrips(Resource):
    """MyTrips class inherits from Resource"""
    def get(self):
        """method get returns all the rides taken or offered by the logged in user"""
        header_token = request.headers.get('Authorization')
        if header_token:
            user_token = header_token.split(" ")[1]
            user_id = User.decode_authentication_token(user_token)

            if isinstance(user_id, int):
                # then get all rides posted by this person using the got id
                user_rides = [ride for ride in rideslist if ride["user_id"] == user_id]

                # get all the ride requests by this person
                user_requests = [user_request for user_request in ride_requests if request["user_id"]==user_id]
                # get the requests details
                return {"status": "success", "message": "successful return",
                        "my_rides": user_rides, "my_requests": user_requests}

        return {"status": "fail", "message": "unregistered user"}, 404
