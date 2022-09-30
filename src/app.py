"""
def sum(a,b):
    return a + b
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!..."

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    nums_sum = a + b
    return "La suma es: " + str(nums_sum)
