from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, Flask!</p>"

@app.route("/name")
def my_name():
    return "<h1>Robert</h1>"