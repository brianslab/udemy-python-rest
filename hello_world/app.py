from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/hithere')
def hi_there():
    return "Welcome to /hithere!"

if __name__=="__main__":
    app.run()
