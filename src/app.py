"""
def sum(a,b):
    return a + b
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!..."

@app.route("/sum/<int:num1>/<int:num2>")
def sum(a: int, b: int):
    return a + b