from flask import Flask, request
from flask_cors import CORS
import os

import socket_serveur as sock_server

app = Flask(__name__)
CORS(app)

@app.route("/screenshot", methods=["POST", "GET"])
def make_a_screeshot():
    print(request.get_data().decode('utf-8'))
    connexion_socket, client_adresse = sock_server.connection()
    response = sock_server.screenshot(connexion_socket)
    return os.getcwd() + "  " +response

app.run(host="localhost", port=12000) 