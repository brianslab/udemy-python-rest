from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from simple_restful!"

if __name__=="__main__":
    app.run(debug=True)
