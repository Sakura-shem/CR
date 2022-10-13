import os, sys, uuid
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
    UID = int(uuid.uuid4())
    return str(UID)[0:16:1]


@scheduler.task('interval', id = 'do_job_1', hours = 3, misfire_grace_time = 900)
def job1():
    DB.ping()


if __name__ == "__main__":
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    app.run(host = '::', port = 8080, debug = True)
