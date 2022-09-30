from distutils.debug import DEBUG
from src.app import app

"""
def main() -> None:
    sum(5,10)
"""

HOST = "localhost"
PORT = 4000
DEBUG = True
    
if __name__ == "__main__":
    app.run(HOST, PORT, DEBUG)