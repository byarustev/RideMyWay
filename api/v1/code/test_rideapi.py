import pytest
import unittest
import rideapi

class TestRide(unittest.TestCase):
    def setUp(self):
        self.app = rideapi.app.test_client()

    def test_get_all_rides(self):
        response = self.app.get('/rides')
        self.assertEqual(response.status_code, 200)
    
    

if __name__=="__main__":
    unittest.main()