"""
def sum(a,b):
    return a + b
"""

from flask import Flask
app = Flask(__name__)

# Bug Solucionado
@app.route("/hello")
def index():
    return "PLSR on Air...."

@app.route("/hello") # Bug Solucionado
def greating(): # Bug Solucionado
    return "Hello World!..."

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    nums_sum = a + b
    return "La suma es: " + str(nums_sum)
