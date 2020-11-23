# import flask module
from flask import Flask

# create App object
app = Flask(__name__)

# if the browser requests the address /, then the app should route that request to this index() function
@app.route('/')

# define a function index() to return "Hello World!!" when the app is executed
def index():
	return '<h1>Hello World!!</h1>'
