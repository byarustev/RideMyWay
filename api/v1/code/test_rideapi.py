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
    
    def test_register_ride(self):
	    # response=self.app.post('/api/v1/rides',data=dict("id"=3,"user_id"=4,"from"="kampala","to"="masaka kavule","dept_date"="14/05/2018","time"="08:30","spots"=4,"description"="this is the third ride"))
	    # response.assertEqual(response.status_code,201)
        pass
        
if __name__=="__main__":
    unittest.main()