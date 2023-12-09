from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/screenshot", methods=["POST", "GET"])
def make_a_screeshot():
    print(request.get_data().decode('utf-8'))
    return os.getcwd()

app.run(host="127.0.0.1", port=12000) 