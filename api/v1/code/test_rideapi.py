import pytest
import unittest
import rideapi
import json

class TestRide(unittest.TestCase):
    def setUp(self):
        self.app = rideapi.app.test_client()

    def test_get_all_rides(self):
        response = self.app.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)
    
    def test_single_ride(self):
        response=self.app.get('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)


if __name__=="__main__":
    unittest.main()