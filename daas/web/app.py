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
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # store username and hashed pw
        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 10
        })

        ret_json = {
            "status": 200,
            "msg": "Successfully signed up for the API"
        }

        return jsonify(ret_json)


def verify_pw(username, password):
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def count_tokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]

    return tokens


class Store(Resource):
    def post(self):
        posted_data = request.get_json()

        username = posted_data["username"]
        password = posted_data["password"]
        sentence = posted_data["sentence"]

        # verify the username and pw match
        correct_pw = verify_pw(username, password)

        if not correct_pw:
            ret_json = {
                "status": 302
            }
            return jsonify(ret_json)

        # verify user has enough tokens
        num_tokens = count_tokens(username)
        if num_tokens <= 0:
            ret_json = {
                "status": 301
            }
            return jsonify(ret_json)

        # store sentence and return 200
        users.update_one({
            "Username": username
        }, {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens - 1
            }
        })

        ret_json = {
            "status": 200,
            "msg": "Sentece saved successfully"
        }
        return jsonify(ret_json)


api.add_resource(Register, '/register')
api.add_resource(Store,  '/store')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
