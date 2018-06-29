from api.modals.user import User
from api.settings.config import ride_requests
from flask import request
from flask_restful import Resource
import sys
import os
sys.path.append(os.path.pardir)


class RequestRide(Resource):
    """class RequestRide extends Resource class methods post"""
    def post(self, ride_id):
        """post method creates a ride request basing on the logged in user"""
        header_token = request.headers.get('Authorization')
        if header_token:
            user_token = header_token.split(" ")[1]
            user_id = User.decode_authentication_token(user_token)

            if isinstance(user_id, int):

                new_ride_request = {"id": (len(ride_requests) + 1), "ride_id": ride_id,
                                    "user_id": user_id, "status": 0}
                ride_requests.append(new_ride_request)
                return {"status": "success", "message": "Request sent"}, 201

        return {"status": "fail", "message": "Request Rejected, Login to request a ride"}, 401
