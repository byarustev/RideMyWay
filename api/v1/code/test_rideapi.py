import pytest
import unittest
import rideapi
import json

from settings import  config


class TestRide(unittest.TestCase):
    def setUp(self):
        self.app = rideapi.app.test_client()

    def test_configuration(self):
        self.assertTrue(config.SECRET_KEY is 'ride_api_key')

    def test_get_all_rides(self):
        response = self.app.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)
    
    def test_single_ride(self):
        response=self.app.get('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        # register user
        response=self.app.post('/api/v1/auth/register',
                                data=json.dumps(dict(email="sample12@mail.com",name="mike",password='12g')),
                                content_type='application/json')
        data=json.loads(response.data.decode())
        # test responce data
        self.assertTrue(data["status"]=="success")
        self.assertTrue(data["auth_token"])
        self.assertEqual(response.status_code, 201)
    
    def test_send_ride_request(self): 
        #register the user
        register_response=self.app.post('/api/v1/auth/register',
                                data=json.dumps(dict(email="sample112@mail.com",name="mike",password="12w")),
                                content_type='application/json')
        register_data=json.loads(register_response.data.decode())
       
        self.assertEqual(register_response.status_code,201)

        #then send request using this person's token
        request_ride=self.app.post('/api/v1/rides/1/requests',
                                headers=dict(
                                    Authorization='requestor '+register_data["auth_token"]
                                ),
                                content_type='application/json')
        request_ride_data=json.loads(request_ride.data.decode())
        self.assertTrue(request_ride_data["status"]=="success")
        self.assertEqual(request_ride.status_code,201)

    def test_login_for_registered_user(self):
        
        # attempt to register user to be used in login
        register_response=self.app.post('/api/v1/auth/register',
                                data=json.dumps(dict(email="sampleas@mail.com",name="mike",password='12g')),
                                content_type='application/json')
        register_data=json.loads(register_response.data.decode())
        #test register
        self.assertTrue(register_data["status"]=="success")
        self.assertTrue(register_data["auth_token"])
        self.assertEqual(register_response.status_code, 201)

        #attempt to login user
        login_response=self.app.post('/api/v1/auth/login',
                                data=json.dumps(dict(email="sampleas@mail.com",name="mike",password='12g')),
                                content_type='application/json')
        login_data=json.loads(login_response.data.decode())

        # test login to a user that has been created on register at the start of the method
        self.assertTrue(login_data["status"]=="success")
        self.assertTrue(login_data["auth_token"])
        self.assertEqual(login_response.status_code, 200)

if __name__=="__main__":
    unittest.main()