
import requests
import json

HOST = "localhost"
BASE_URL = f"http://{HOST}:12000"

# obtenir le repertoire courant
response = requests.get(f"{BASE_URL}/get_current_dir")
data = json.loads(response.content)
dir = data[0]
filenames = json.loads(data[1]) 
print(dir)
[print(filenames[i]) for i in range(len(filenames))]



# aller en arrière
result = requests.get(f"{BASE_URL}/go_back")
print(json.loads(result.content.decode()))



# screenshot
result = requests.get(f"{BASE_URL}/screenshot")
print(result.content.decode())



# télécharger un fichier
response = requests.get(f"{BASE_URL}/get_current_dir")
data = json.loads(response.content)
dir = data[0]
filenames = json.loads(data[1]) # devra recevoir un filename
file_path = json.dumps("\\".join((dir, str(filenames[1])))) 
result = requests.get(f"{BASE_URL}/download", data=file_path)  # devra recevoir un file path 
print()
print(result.content.decode("utf-8"))



# aller dans un dossier
response = requests.get(f"{BASE_URL}/get_current_dir")
data = json.loads(response.content)
dir = data[0]
filenames = json.loads(data[1]) 
result = requests.get(f"{BASE_URL}/go_dir", data=filenames[0])  # devra recevoir un filename
print()
print(result.content.decode("utf-8"))



# executer un programme
response = requests.get(f"{BASE_URL}/get_current_dir")
data = json.loads(response.content)
dir = data[0]
filenames = json.loads(data[1]) 
result = requests.get(f"{BASE_URL}/execute", data=filenames[2])
print(result.content.decode("utf-8"))



# envoyer une ligne de commande custom
command = "ipconfig"
response = requests.get(f"{BASE_URL}/custom", data=command)  # devra recevoir une commande
print()
print(response.content.decode("utf-8"))

