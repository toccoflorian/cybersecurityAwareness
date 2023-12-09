import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"Attente de connexion de {HOST_IP} port: {HOST_PORT}")
connexion_socket, client_adresse = s.accept()
print("connecter")

s.sendall("salut".encode(), 5)
time.sleep(500)

# Aller dans un répertoire et revenir en arrière

# télécharger un fichier

# Executer un fichier

# prendre une capture d'écran
def screenshot():
    

# détruire la machine distante

# envoyer une ligne de commande custom