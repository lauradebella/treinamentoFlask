# We need to import the jsonify object, it will let us
# output json, and it will take care of the right string
# data conversion, the headers for the response, etc
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

#http://code.runnable.com/UiIDW0LvVMFPAAAM/how-to-return-json-from-flask-for-python

# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80")
    )
