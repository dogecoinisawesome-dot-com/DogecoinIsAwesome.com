from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def homepage():
    try:
        return render_template("index.html")
    except IndexError:
        abort(404)