from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to DogecoinIsAwesome.com!"