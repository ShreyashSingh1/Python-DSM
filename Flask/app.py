from flask import Flask, render_template
from flask import request, jsonify

"""
Flask allows you to create APIs that can be accessed using URLs. 
Flask is a popular web framework for building web applications and APIs in Python.
"""

"""
Client side: GET,POST -> Sending data
GET -> Data is passed with help of URL by System to the server  eg.Google search -> search, Data Science
POST -> Data is passed as a body by System to the server  eg.Gmail login
"""

app = Flask(__name__)

# Route binding
@app.route('/')
def home_page():
    return render_template('index.html')

"""
methods=["POST"] indicates that the route is configured to 
handle only HTTP POST requests. This means that when a client sends an 
HTTP POST request to the specified URL, the associated function or 
view will be executed to process the request.
"""

@app.route("/math", methods=["POST"])
def math_operation():
    
    if request.method == "POST":
        ops = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        if ops == "add":
            r = num1 + num2
            result = f"The Sum of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "subtract":
            r = num1 - num2
            result = f"The subtraction of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "multiply":
            r = num1 * num2
            result = f"The multiplication of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "divide":
            r = num1 / num2
            result = f"The division of {str(num1)} and {str(num2)} is {str(r)}"

        return render_template("results.html", result = result)
 
            
@app.route("/postman_data", methods=["POST"])
def math_operation_pman():
    
    if request.method == "POST":
        ops = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        if ops == "add":
            r = num1 + num2
            result = f"The Sum of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "subtract":
            r = num1 - num2
            result = f"The subtraction of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "multiply":
            r = num1 * num2
            result = f"The multiplication of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "divide":
            r = num1 / num2
            result = f"The division of {str(num1)} and {str(num2)} is {str(r)}"

        return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
