from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sys, os
sys.path.append(os.path.pardir)
from api.modals.user import User
from api.settings.config import  rideslist,users_list,ride_requests

class RegisterUser(Resource):
    """RegisterUser extends Resource class methods post for creating a new user"""
    def post(self):
        """RideResource2 extends Resource class methods post for creating a ride join request"""
        
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="name is required")
        parser.add_argument('email', type=str, required=True, help="email is required")
        parser.add_argument('password', type=str, required=True, help="password field is required")
        parser.add_argument('confirm', type=str, required=True, help="password confirmation is required")
        data = parser.parse_args()

        #get the
        user_emails_mappings = {user.email: user for user in users_list}
        user_mail = user_emails_mappings.get(data["email"], None)

        if data["password"]!=data["confirm"]:
            return {"status":"fail","message":"password mismatch"}, 400
        
        if not user_mail:
            # create user
            temp_user = User((len(users_list) + 1), data["name"], data["email"], data["password"],data['confirm'])
            users_list.append(temp_user)
            # get auth token
            auth_token = temp_user.encode_authentication_token(temp_user.id)
            return {"auth_token":auth_token.decode(), "status":"success",
                    "message":"account created"}, 201
        return {"status":"fail", "message":"email already taken"}, 400
