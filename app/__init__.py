import os

from flask import Flask

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__, static_folder="static", static_url_path="")

from app import routes
