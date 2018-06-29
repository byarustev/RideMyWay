from pprint import pprint
from api.db import DataBaseConnection


class Ride:
    def __init__(self, ride_id, user_id, origin, destination, departure_time, slots, description):
        self.ride_id = ride_id
        self.user_id = user_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.slots = slots
        self.description = description

    @staticmethod
    def create_ride(ride):
        query_string = """
                      INSERT INTO rides (user_id, origin, destination, departure_time, slots, description) 
                      VALUES (%s,%s,%s,%s,%s,%s)
                      """
        try:
            # create connection and set cursor
            connection = DataBaseConnection()
            cursor = connection.cursor
            cursor.execute(query_string, (ride.user_id, ride.origin, ride.destination, 
                                          ride.departure_time, ride.slots, ride.description))
        except Exception as exp:
            pprint(exp)
        
    @staticmethod
    def get_all_rides():
        query_string = """
                     SELECT * FROM rides
                     """
        try:
            connection = DataBaseConnection()
            cursor = connection.dict_cursor
            cursor.execute(query_string)
            return cursor.fetchmany()

        except Exception as exp:
            pprint(exp)
            return None
