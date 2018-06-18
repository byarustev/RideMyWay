from flask import Flask,request, jsonify
from flask_restful import Api,Resource
import user

app=Flask(__name__)

api=Api(app)

rideslist=[
            {"id":1,"from":"kampala","to":"masaka kavule","dept_date":"14/05/2018","time":"08:30","spots":5,"description":"this is the first ride"},
            {"id":2,"from":"sudan","to":"kasese","dept_date":"13/05/2018","time":"09:30","spots":2,"description":"this is the second ride"},
            {"id":3,"from":"kampala","to":"masaka kavule","dept_date":"14/05/2018","time":"08:30","spots":4,"description":"this is the third ride"}
            ]

class RidesListResource(Resource):
    def get(self):
        """returns a ride with the passed id"""
        return {"rides":rideslist},200

class RideResource(Resource):
    def get(self,ride_id):
        """returns a ride matching a given id""" 

        ride=[x for x in rideslist if x["id"]==ride_id]
        if ride:
            return {"status":"success","ride":ride,"message":"ride found"},200
        else:
            return {"status":"fail","message":"Ride Not Found"},404

    def post(self):
        data=request.get_json()
        temp_ride={"id":(len(rideslist)+1),
                    "from":data["from"],
                    "to":data["to"],
                    "dept_date":data["date"],
                    "time":data["time"],
                    "slots":data["slots"],
                    "description":data["description"]}
        rideslist.append(temp_ride)

        return {"status":"success"},201

api.add_resource(RidesListResource,'/api/v1/rides') #get all rides
api.add_resource(RideResource,'/api/v1/rides/<int:ride_id>','/api/v1/rides') #get a particular ride

if __name__ == "__main__":
    app.run(debug=True)    
