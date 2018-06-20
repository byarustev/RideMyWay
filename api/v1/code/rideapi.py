"""
File for Api logic
"""
#custom files imports
from user import User

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

APP = Flask(__name__)
API = Api(APP)

rideslist = [
    {"id":1, "user_id":2, "from":"kampala", "to":"masaka kavule",
     "dept_date":"14/05/2018", "time":"08:30", "spots":5, "description":"this is the first ride"}
    ]

# for every user their id, name, email and password are captured
users_list = [User(1, "Mike", "mail1@example.com", "1234")]

#each ride request contains the id of the ride, the id of the
#person requesting and the acceptance status
#0 for pending 1 for accepted and 2 for rejected
ride_requests = [{"id":1, "ride_id":2, "user_id":1, "status":0}]

class RidesListResource(Resource):
    """RidesListResource extends Resource class methods get"""
    def get(self):
        """returns a ride with the passed id"""
        return {"rides":rideslist}, 200

class RideResource2(Resource):
    """class RideResource2 extends Resource class methods post for creating a ride join request"""
    def post(self, ride_id):
        """post method creates a ride request basing on the logged in user"""
        header_token = request.headers.get('Authorization')
        if header_token:
            user_token = header_token.split(" ")[1]
            user_id = User.decode_authentication_token(user_token)

            if isinstance(user_id, int):
                #id generated by increamenting the
                new_ride_request = {"id":(len(ride_requests) + 1), "ride_id":ride_id,
                                    "user_id":user_id, "status":0}
                ride_requests.append(new_ride_request)
                return {"status":"success", "message":"Request sent"}, 201

        return {"status":"fail", "message":"Request Rejected, Login to request a ride"}, 401

class RideResource(Resource):
    """class RideResource extends Resource class methods get
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
        parser.add_argument('from', type=str, required=True, help="this field is required")
        parser.add_argument('to', type=str, required=True, help="this field is required")
        parser.add_argument('date', type=str, required=True, help="this field is required")
        parser.add_argument('time', type=str, required=True, help="this field is required")
        parser.add_argument('slots', type=str, required=True, help="this field is required")
        parser.add_argument('description', type=str, required=True, help="this field is required")

        data = parser.parse_args()

        temp_ride = {"id":(len(rideslist) + 1),
                     "from":data["from"],
                     "user_id":4, #needs to change to currently logged in user
                     "to":data["to"],
                     "dept_date":data["date"],
                     "time":data["time"],
                     "slots":data["slots"],
                     "description":data["description"]}
        rideslist.append(temp_ride)

        return {"status":"success"}, 201

class RegisterUser(Resource):
    """RegisterUser extends Resource class methods post for creating a new user"""
    def post(self):
        """RideResource2 extends Resource class methods post for creating a ride join request"""
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help="this field is required")
        parser.add_argument('password', type=str, required=True, help="this field is required")
        data = parser.parse_args()

        #get the
        user_emails_mappings = {user.email: user for user in users_list}
        user_mail = user_emails_mappings.get(data["email"], None)

        if not user_mail:
            # create user
            temp_user = User((len(users_list) + 1), data["name"], data["email"], data["password"])
            users_list.append(temp_user)
            # get auth token
            auth_token = temp_user.encode_authentication_token(temp_user.id)
            return {"auth_token":auth_token.decode(), "status":"success",
                    "message":"account created"}, 201
        return {"status":"fail", "message":"email already taken"}, 400

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

API.add_resource(RidesListResource, '/api/v1/rides') #get all rides
API.add_resource(RideResource, '/api/v1/rides/<int:ride_id>', '/api/v1/rides')
API.add_resource(RegisterUser, '/api/v1/auth/register') #register a user
API.add_resource(LoginUser, '/api/v1/auth/login') #register a user
API.add_resource(RideResource2, '/api/v1/rides/<int:ride_id>/requests')

if __name__ == "__main__":
    APP.run(debug=True)
