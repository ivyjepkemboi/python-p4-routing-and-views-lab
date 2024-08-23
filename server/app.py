#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# Route for the base URL
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# printing a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter  

# counting up to a given integer
@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

# Route for performing math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
   
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
