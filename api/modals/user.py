import datetime
import jwt
# import custom file config
from api.settings import  config

class User():
    """User class defines the methods needed by user and the attributes.
        on creation pass in id,name,email,password"""
    def __init__(self, _id, name, email, password,confirm):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password
        self.confirm = confirm
    @staticmethod
    def encode_authentication_token(user_id):
        """generates authentication token for a particular user"""
        try:
            payload = {"exp":datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=120),
                       "iat":datetime.datetime.utcnow(),
                       "sub":user_id}
            return jwt.encode(payload, config.SECRET_KEY, algorithm='HS256') #algorithm for signing
        except Exception as exp:
            return exp

    @staticmethod
    def decode_authentication_token(auth_token):
        """Decodes the auth_token into the user id and returns the user id"""

        try:
            payload = jwt.decode(auth_token,config.SECRET_KEY)
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return "Token Expired. Please Login Again"
        
        except jwt.InvalidTokenError:
            return "Invalid token. Please Login Again"
    
    def insert_user_data(self,cursor,name,email,password):
        query_string="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        cursor.execute(query_string,(name,email,password))
        return 
            
