import subprocess
import time
import backend.serveur.server

print("main")

time.sleep(2)

try:
    # Démmarer le serveur Vite
    s = subprocess.run("start cmd /k server.exe", shell=True, capture_output=False, universal_newlines=True)
    subprocess.run("npm i", shell=True, capture_output=False, universal_newlines=True)
    subprocess.run("npm run dev", shell=True, capture_output=False, universal_newlines=True)
        # Démmarer le serveur Flask
    print(s)
    time.sleep(100)
except Exception as e:
    print(e.args)
    time.sleep(1000)