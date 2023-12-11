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
    resultat = fonctions.lister_contenu()
    return json.dumps((os.getcwd(), resultat))


# aller dans un dossier
@app.route("/go_dir", methods=["POST", "GET"])
def go_dir():
    r = request.get_data()
    try:
        os.chdir("\\".join((os.getcwd(), r.decode("utf-8"))))
        resultat = fonctions.lister_contenu()
        return json.dumps(resultat)
    except:
        return json.dumps(f"{r.decode('utf-8')} n'éxiste pas dans ce dossier.")


# aller dans le dossier parent
@app.route("/go_back", methods=["GET", "POST"])
def go_back():
    os.chdir("\\".join(os.getcwd().split("\\")[:-1]))
    resultat = fonctions.lister_contenu()
    return json.dumps((os.getcwd(), resultat))
    

# executer un programme
@app.route("/execute", methods=["POST", "GET"])
def execute():
    r = request.get_data()
    try:
        process = subprocess.run(r.decode("utf-8"), shell=True, capture_output=True, universal_newlines=True)
        print(["Commande executer avec succes! ", ["RETOUR: ", process.stderr, r.decode("utf-8") + " executer avec succes! "]])
        return json.dumps(["Commande executer avec succes! ", ["RETOUR: ", process.stderr, "" if process.stderr else r.decode("utf-8") +  " executer avec succes!"]])
    except:
        print("Impossible d'executer " + str(r.decode("ascii", 'replace'))  + " !")
        return json.dumps("Impossible d'executer " + str(r.decode("ascii", 'replace'))  + " !")
    

    # commande custom
@app.route("/custom", methods=["POST", "GET"])
def custom():
    r = request.get_data()
    command = r.decode("utf-8")
    result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
    out = result.stdout
    err = result.stderr
    print(out)
    print("err:", result)
    if int(result.returncode) == 1:
        return err.encode("utf-8")
    else:
        return out.encode("utf-8")
    


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
    r = request.get_data()
    filename = "./" + r.decode("utf-8")[:-1]
    print(filename)
    f = open(filename, "rb")
    data = f.read()
    f.close()
    return data



if __name__ == "__main__":
    app.run(host="localhost", port=12001)


