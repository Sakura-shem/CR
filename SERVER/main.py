import uuid
from flask import Flask

app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def main():
    return "~~~"

@app.route("/register" , methods = ["POST"])
def name():
    UID = int(uuid.uuid4())
    return str(UID)[0:16:1]

app.run(host = '::', port = 8080, debug = True)
