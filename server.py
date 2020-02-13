from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "hello!"

port = "5000"

if "PORT" in os.environ:
    port = os.environ["PORT"]

app.run(port=port, host="0.0.0.0")
