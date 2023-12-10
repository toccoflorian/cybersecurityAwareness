import subprocess
import os
import platform
import datetime
from PIL import ImageGrab

# prendre une capture d'écran et l'envoyer au serveur
def screenshot():
    try:
        # Chemin du dossier contenant le script actuel
        base_dir = os.path.dirname(os.path.abspath(__file__))
        dir = base_dir + "\screenshots\\"
        filename = "Capture_" + datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y_%Hh%Mm%Ss") + ".png"
        
        ImageGrab.grab().save(dir + filename, "png")
        print("screeshot succes")
        return True, f"{filename} enregistré dans le répertoire: {dir}"
    except:
        print("screenshot fail")
        return False, "L'image n'as pas pu être capturée!"



def lister_contenu():

    # Lister le contenu du répertoire courant
    contenu = os.listdir('.')
    dossiers_et_fichiers = []
    for item in contenu:
        if os.path.isdir(item):
            dossiers_et_fichiers.append(item)
        else:
            dossiers_et_fichiers.append(item + "@")

    return dossiers_et_fichiers if dossiers_et_fichiers != "" else False

# screenshot()
# print()