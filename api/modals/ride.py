from api.settings import  config
from pprint import pprint

class Ride:
    def __init__(self,ride_id,user_id,origin,destination,departure_time,slots,description):
        self.ride_id = ride_id
        self.user_id=user_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.slots = slots
        self.description = description
    @staticmethod
    def create_ride(cursor,ride):
        query_string="""
                     INSERT INTO rides (user_id, origin, destination, departure_time, slots, description) 
                     VALUES (%s,%s,%s,%s,%s,%s)
                     """
        try:
            cursor.execute(query_string, (ride.user_id, ride.origin, ride.destination, 
                                          ride.departure_time, ride.slots, ride.description))
        except Exception as exp:
            pprint(exp)
        
        