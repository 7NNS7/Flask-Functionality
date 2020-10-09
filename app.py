print('Starting to import the packages')
import flask
from flask import request

from dependencies import Dependenciesnow
print('Imported the packages and now creating the flask app.')
app = flask.Flask(__name__)
var = Dependenciesnow()
print("Flask app has been created.")
@app.route('/',methods=['GET'])
def hello_world():
    print("Inside hello world")
    return "Hi"
print("App will now run.")
app.run('0.0.0.0',port = 1234,debug=True)