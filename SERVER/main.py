import os, sys, uuid, json
from flask import Flask
path = [os.path.dirname(__file__), os.path.dirname(__file__) + "\Database"]
for i in path:
    sys.path.append(i)
from Database import DBConnecter
from Scheduler import Config, scheduler



app = Flask(__name__)
DB = DBConnecter("root", "DB666SHEM", "CR")

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

@scheduler.task('interval', id = 'do_job_1', hours = 3, misfire_grace_time = 900)
def job1():
    DB.ping()


if __name__ == "__main__":
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    app.run(host = '127.0.0.1', port = 8080, debug = True)
