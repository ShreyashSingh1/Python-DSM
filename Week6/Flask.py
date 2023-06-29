"""
Flask is commonly used for developing web applications and RESTful APIs.
And to expose our functions to the outer world so that is can be accessed from anywhere
Helps in making server side
"""
from flask import Flask
from flask import request

# app is object of flask
app = Flask(__name__)

"""
When client reaches to server side
Flask will provide route for client side to access to these functions  
Route provides a to access a particular function
"""

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World 1!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World 2!</h1>"

@app.route("/test")
def test():
    a = 5 + 7
    return f"This is my function to run app {a}"

"""
It takes input in url then execute (kwy value hai)
This how we give input
http://192.168.0.104:5000/test2/test2?x=Shreyash
"""
@app.route("/test2/test2")
def test2():
    data = request.args.get("x")
    return f"This is data input from my url {data}"

if __name__ == "__main__":
    """app.run() starts the Flask development server and listens for 
    incoming requests from clients. The host parameter specifies the 
    network interface the server should bind to. In this case, "0.0.0.0" 
    means the server will listen on all available network interfaces. 
    This allows the server to accept requests from any IP address."""
    app.run(host="0.0.0.0")
