import unittest

# This is the class we want to test. So, we need to import it


from app import database
import json
import os
from os import path

import tweepy
import datetime as dt
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from dotenv import load_dotenv
from textblob import TextBlob
import pandas as pd
import numpy as np
from app.config import InitConfig
from app.models.HashtagModel import HashtagModel
from app.models.TwitterSentimentAnalysisModel import TwitterSentimentAnalysisModel
from app.models.UserModel import UserModel
from app.services.GetColorBySentimentService import GetColorBySentimentService


class Usermodel():

    def __init__(self):
        self.sql = SQL()
        self.filename = "app\database\TwitterDB.db"
        self.db_location = os.path.join(os.getcwd(), self.filename)

    class TestCase(unittest.TestCase):
        def setUp(self, username):
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            TwitterDB.create_all()
            self.app = app.test_client()

        def tearDown(self):
            TwitterDB.session.remove()
            TwitterDB.drop_all(bind='__all__')
            TwitterDB.drop_all()

    class TestUserModel(TestCase):
        usermodel = UserModel()  # instantiate

    def index(self, username):
        return self.app.post('/index', data=dict(usename=username), follow_redirects=True)

    def test_promote_user(self, username):
        index = UserModel(username='RaiP')
        TwitterDB.session.add(index)
        TwitterDB.session.commit()
        response = self.index(username='RaiP')
        self.assertIn(b'You have been logged in!', response.data)

    def test_demote_user(self, username):
        index = UserModel(username='RaiP')
        TwitterDB.session.add(index)
        TwitterDB.session.commit()
        response = self.index(username='RaiP')
        self.assertIn(b'You have been logged in!', response.data)

        def test_create_user(self, username, password,email,phone,first_name,last_name,address,registration_no, speciality):
            index1 = username(username='RaiP', password='1234', email='raipolley1@gmail.com', phone='9804012207', first_name='rai', last_name='polley',address='kolkata', registration_no='123', speciality='cse')
            TwitterDB.session.add(index1)
            TwitterDB.session.commit()
            response = self.index1(username='RaiP', password='1234', email='raipolley1@gmail.com', phone='9804012207', first_name='rai', last_name='polley',address='kolkata', registration_no='123', speciality='cse')
            self.assertIn(b'You have been logged in!', response.data)
            print()



if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
