
import uuid
from flask import Flask

app = Flask(__name__)
@app.route("/register" , methods = ["POST"], endpoint = "")
def name():
    UID = int(uuid.uuid4())
    return str(UID)[0:16:1]

app.run(host='127.0.0.1', port = 8080, debug = True)
