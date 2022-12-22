from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):
        # resource Add was requested with POST
        postedData = request.get_json()
        x = int(postedData["x"])
        y = int(postedData["y"])

        result = x + y
        resultJSON = {
            'Status Code': 200,
            'Message': result
        }
        return jsonify(resultJSON)


class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello from simple_restful!"

if __name__=="__main__":
    app.run(debug=True)
