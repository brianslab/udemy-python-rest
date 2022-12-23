from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, function):
    if (function in ['add', 'subtract', 'multiply']):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif (function == 'divide'):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "add")

        if (statusCode != 200):
            resultJSON = {
                'Message': 'An error has occured',
                'Status Code': statusCode
            }
            return jsonify(resultJSON)

        x = int(postedData["x"])
        y = int(postedData["y"])

        result = x + y
        resultJSON = {
            'Status Code': 200,
            'Message': result
        }
        return jsonify(resultJSON)


class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "subtract")

        if (statusCode != 200):
            resultJSON = {
                'Message': 'An error has occured',
                'Status Code': statusCode
            }
            return jsonify(resultJSON)

        x = int(postedData["x"])
        y = int(postedData["y"])

        result = x - y
        resultJSON = {
            'Status Code': 200,
            'Message': result
        }
        return jsonify(resultJSON)


class Multiply(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "multiply")

        if (statusCode != 200):
            resultJSON = {
                'Message': 'An error has occured',
                'Status Code': statusCode
            }
            return jsonify(resultJSON)

        x = int(postedData["x"])
        y = int(postedData["y"])

        result = x*y
        resultJSON = {
            'Status Code': 200,
            'Message': result
        }
        return jsonify(resultJSON)


class Divide(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "divide")

        if (statusCode != 200):
            resultJSON = {
                'Message': 'An error has occured',
                'Status Code': statusCode
            }
            return jsonify(resultJSON)

        x = int(postedData["x"])
        y = int(postedData["y"])

        result = (x*1.0)/y
        resultJSON = {
            'Status Code': 200,
            'Message': result
        }
        return jsonify(resultJSON)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


@ app.route('/')
def hello_world():
    return "Hello from simple_restful!"


if __name__ == "__main__":
    app.run(debug=True)
