from flask import Flask,request, jsonify
from flask_restful import Api,Resource

app=Flask(__name__)

api=Api(app)

rideslist=[
            {"id":1,"from":"kampala","to":"masaka kavule","dept_date":"14/05/2018","time":"08:30","spots":5,"description":"this is the first ride"},
            {"id":2,"from":"sudan","to":"kasese","dept_date":"13/05/2018","time":"09:30","spots":2,"description":"this is the second ride"},
            {"id":3,"from":"kampala","to":"masaka kavule","dept_date":"14/05/2018","time":"08:30","spots":4,"description":"this is the third ride"}
            ]

class Ride(Resource):
    def get(self):
        """returns a ride with the passed id"""
        return {"rides":rideslist},200
       

api.add_resource(Ride,'/rides') #get a particular ride

if __name__ == "__main__":
    app.run(debug=True)    
