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
        posted_data = request.get_json()

        # get the username and password
        # assume valid input
        username = posted_data["username"]
        password = posted_data["password"]

        # hash the password
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        # store username and hashed pw
        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": ""
        })

        ret_json = {
            "status": 200,
            "msg": "Successfully signed up for the API"
        }

        return jsonify(ret_json)


api.add_resource(Register, '/register')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
