from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sys, os

sys.path.append(os.path.pardir)

from api.modals.user import User
from api.settings.config import  rideslist,users_list,ride_requests
from api.db import DataBaseConnection 

class LoginUser(Resource):
    """LoginUses extends Resource methods post which logins i given user"""
    def post(self):
        """logins in a given user"""
        #parse arguments to ensure that required fields are sent
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help="this field is required")
        parser.add_argument('password', type=str, required=True, help="this field is required")

        data = parser.parse_args()
        
        # create connection and set cursor
        con=DataBaseConnection()
        dict_cursor=con.dict_cursor

        user_data=User.get_user_by_email(dict_cursor,data["email"])

        if user_data:
            #find if the user passwords match
            if user_data["password"] == data["password"]:
                # generate token
                auth_token = User.encode_authentication_token(user_data['user_id'])
                return {"status":"success", "message":"suceesful login",
                        "auth_token":auth_token.decode()}, 200
                        
        #if no return till this point then the user was not found
        return {"status":"fail", "message":"invalid user name or password"}, 401
