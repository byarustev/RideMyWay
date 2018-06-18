import jwt
import unittest
import pytest
from user import *
from settings import  config


class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_user=User(1,'example@mail.com','12345')
        
    def test_authentication_encoding(self):
        auth_token=self.test_user.encode_authentication_token(self.test_user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        
    def test_authentication_decoding(self):
        auth_token=self.test_user.encode_authentication_token(self.test_user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_authentication_token(auth_token),1)