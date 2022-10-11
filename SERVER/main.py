
import uuid
from flask import Flask

app = Flask(__name__)
@app.route("/register" , methods = ["POST"], endpoint = "")
def name():
    UID = uuid.uuid1()
    return UID

app.run(debug = True)
