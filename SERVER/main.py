import os, sys, uuid
from flask import Flask
path = os.path.dirname(__file__) + "\Database"
sys.path.append(path)
from Database import DBConnecter

app = Flask(__name__)
DB = DBConnecter("root", "DB666SHEM", "CR")

@app.route("/" , methods = ["GET"])
def main():
    return "~~~"

@app.route("/register" , methods = ["POST"])
def name():
    UID = int(uuid.uuid4())
    return str(UID)[0:16:1]

app.run(host = '::', port = 8080, debug = True)
