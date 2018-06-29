from api.modals.ride import Ride
from flask_restful import Resource
import sys
import os
sys.path.append(os.path.pardir)


class RidesList(Resource):
    """RidesList extends Resource class methods get """
    def get(self):
        """returns all the rides in the system"""
        rides = []
        rows = Ride.get_all_rides()
        for row in rows:
            temp_ride = Ride(row["ride_id"], row["user_id"], row["origin"], row["destination"],
                             str(row["departure_time"]), row["slots"], row["description"])
            rides.append(temp_ride.__dict__)
        return {"rides": rows}, 200
