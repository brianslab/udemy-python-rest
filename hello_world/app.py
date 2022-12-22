from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/hithere')
def hi_there():
    return "Welcome to /hithere!"

@app.route('/json')
def json_example():
    age = 2022 - 1996
    retJson = {
        'Name': 'Brian',
        'Age': age,
        'pets': [
            {
                'name': 'Greg',
                'type': 'cat'
            },
            {
                'name': 'Sofi',
                'type': 'cat'
            }

        ]
    }
    return jsonify(retJson)

@app.route('/add', methods=["POST"])
def add_two_nums():
    data = request.get_json()
    x = data["x"]
    y = data["y"]

    z = x + y

    retJSON = {
        "z": z
    }

    return jsonify(retJSON), 200

if __name__=="__main__":
    app.run(debug=True)
