import os, sys, uuid, json
from flask import Flask, request
path = [os.path.dirname(__file__), os.path.dirname(__file__) + "\Database"]
for i in path:
    sys.path.append(i)
from Database import DBConnecter
from Scheduler import Config, scheduler

app = Flask(__name__, static_folder = os.path.dirname(__file__) + '\static')

DB = DBConnecter("root", "DB666SHEM", "CR")
host = '127.0.0.1'
port = 8080

@app.route("/" , methods = ["GET"])
def main():
    return "~~~"

@app.route("/register" , methods = ["POST"])
def name():
    UID = str(int(uuid.uuid4()))[0:16:1]
    return UID

@app.route("/roomlist" , methods = ["POST"])
def roomlist():
    rooms = DB.roominfo()
    return json.dumps(rooms)

@app.route("/roompic" , methods = ["GET"])
def roompic():
    id = request.args.get("roomid")
    path = f"http:/{host}:{port}/static/room/{id}/{id}.jpg"
    return path

@app.route("/visiterpic" , methods = ["GET"])
def visiterpic():
    path = [f"http:/{host}:{port}/static/user/visiter/0.jpg", f"http:/{host}:{port}/static/user/visiter/1.jpg"]
    return json.dumps(path)

@app.route("/userpic" , methods = ["GET"])
def userpic():
    id = request.args.get("userid")
    path = f"http:/{host}:{port}/static/user/{id}/{id}.jpg"
    return path

@scheduler.task('interval', id = 'do_job_1', hours = 3, misfire_grace_time = 900)
def job1():
    DB.ping()


if __name__ == "__main__":
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    app.run(host = host, port = port, debug = True)
