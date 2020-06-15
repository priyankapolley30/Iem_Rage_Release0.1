import unittest




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
from flask import Flask
from flask_cors import CORS

from app.controllers.v1 import version1

app = Flask(__name__)

cors = CORS(application, resources={r"/*": {"origins": "*"}}, support_credentials=True)
application.config["CORS_HEADERS"] = 'application/json'
application.register_blueprint(version1,url_prefix="/twitter-sentiment-analysis/v1")

class FlaskTest(unittest.TestCase):
    
    def test_create_users(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/users")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
                  
     def test_login(self):
        tester = app.test_client(self)
        response = tester.post("http://localhost:5000/twitter-sentiment-analysis/v1/login",data=json.dumps(dict(usename='RaiP',password='12345')),content_type='application/join')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
       
     def test_analysis(self):
        tester = app.test_client(self)
        response = tester.post("http://localhost:5000/twitter-sentiment-analysis/v1/analysis")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        

     def test_get_twitter_users_data(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/get-twitter-users-data")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
     def test_hashtags(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/hashtags")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        
      
     def test_create_hashtags(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/create-hashtag")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

        
     def test_activate_hashtags(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/activate-hashtag/suicide")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
      
      
     def test_deactivate_hashtags(self):
        tester = app.test_client(self)
        response = tester.get("http://localhost:5000/twitter-sentiment-analysis/v1/deactivate-hashtag/suicide")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
