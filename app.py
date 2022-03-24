import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "<h1>TEST HELLO</h1>"


if __name__ == "__main__":
    try:
        os.system('flask run')
    except KeyboardInterrupt:
        print("Application terminé.")