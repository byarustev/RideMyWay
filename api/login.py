from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sys, os

sys.path.append(os.path.pardir)

from api.modals.user import User
from api.settings.config import  rideslist,users_list,ride_requests

class LoginUser(Resource):
    """LoginUses extends Resource methods post which logins i given user"""
    def post(self):
        """logins in a given user"""
        #parse arguments to ensure that required fields are sent
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help="this field is required")
        parser.add_argument('password', type=str, required=True, help="this field is required")

        data = parser.parse_args()
        user_emails_mappings = {user.email: user for user in users_list}
        user_mail = user_emails_mappings.get(data["email"], None)

        if user_mail:
            #find if the user passwords match
            for temp_user in users_list:
                if temp_user.email == user_mail.email:
                    if temp_user.password == data["password"]:
                        # generate token
                        auth_token = temp_user.encode_authentication_token(temp_user.id)
                        return {"status":"success", "message":"suceesful login",
                                "auth_token":auth_token.decode()}, 200

        #if no return till this point then the user was not found
        return {"status":"fail", "message":"invalid user name or password"}, 401
