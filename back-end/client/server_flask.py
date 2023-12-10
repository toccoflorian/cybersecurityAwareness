import datetime
import json
import os
import subprocess
from flask import Flask, request
from flask_cors import CORS
from PIL import ImageGrab

import fonctions


app = Flask(__name__)

# obtenir le repertoire courant
@app.route("/get_current_dir", methods=["GET", "POST"])
def receive_command():
    resultat = json.dumps(fonctions.lister_contenu())
    return json.dumps((os.getcwd(), resultat))

# aller en arrière
@app.route("/go_back", methods=["GET", "POST"])
def go_back():
    os.chdir("\\".join(os.getcwd().split("\\")[:-1]))
    resultat = fonctions.lister_contenu().encode()
    return resultat
    # response = subprocess.run(command.decode(), shell = True, capture_output = True, universal_newlines = True)
    # error = response.stderr
    # out = response.stdout
    # return out if out else error


# screenshot
@app.route("/screenshot", methods=["GET", "POST"])
def screeshot():
    filename = "Capture_" + datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y_%Hh%Mm%Ss") + ".png"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir = base_dir + "\\client\\temporary\\"
    capture = ImageGrab.grab()
    capture.save(dir + filename, "PNG")
    f = open(dir + filename, "rb")
    response = f.read()
    f.close()
    os.remove(dir + filename)
    return response


# download
@app.route("/download", methods=["POST", "GET"])
def download():
    pass

if __name__ == "__main__":
    app.run(host="localhost", port=12001)
