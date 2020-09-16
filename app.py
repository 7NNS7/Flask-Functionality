import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    #print("Inside Hello World!")
    if request.environ['SERVER_PROTOCOL'] != "HTTP/1.1":
        flask.abort(406)
        return "Access Denied"
    else:
        return "Hello Word"
    print(request.environ['SERVER_PROTOCOL'])
    #return "Hello"

app.run('0.0.0.0',port = 5555,debug=True)