from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sys, os
sys.path.append(os.path.pardir)

from api.settings.config import  rideslist,users_list,ride_requests

class RidesList(Resource):
    """RidesList extends Resource class methods get """
    def get(self):
        """returns a ride with the passed id"""
        return {"rides":rideslist}, 200
