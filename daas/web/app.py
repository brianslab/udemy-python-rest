"""
Register a user with 0 tokens
give them 10 tokens
store/retriving sentences costs 1 token
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDB
users = db["Users"]


class Register(Resource):
    def post(self):
        postedData = request.get_json()

        # get the username and password
        # assume valid input
        username = postedData["username"]
        password = postedData["password"]

        # hash the password
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        # store username and hashed pw
        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": ""
        })
