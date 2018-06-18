import jwt
import datetime

from settings import  config

class User():
    def __init__(self,_id,email,password):
        self.id=_id
        self.email=email
        self.password=password
    def encode_authentication_token(self,user_id):
        """generates authentication token for a particular user"""
        try:
            payload={"exp":datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                "iat":datetime.datetime.utcnow(),
                "sub":user_id}
            return jwt.encode(payload,config.SECRET_KEY,algorithm='HS256') #algorithm for signing
        except Exception as exp:
            return exp

    @staticmethod
    def decode_authentication_token(auth_token):
        """Decodes the auth_token into the user id and returns the user id"""

        try:
            payload=jwt.decode(auth_token,config.SECRET_KEY)
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return "Token Expired. Please Login Again"
        
        except jwt.InvalidTokenError:
            return "Invalid token. Please Login Again"
