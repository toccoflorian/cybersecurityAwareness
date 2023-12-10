
import requests
import json

# # obtenir le repertoire courant
# response = requests.get("http://localhost:12000/get_current_dir")
# data = json.loads(response.content)
# dir = data[0]
# filenames = json.loads(data[1]) 
# print(dir)
# print(filenames[0])

# # aller en arrière
# result = requests.get("http://localhost:12000/go_back")
# print(json.loads(result.content.decode()))

# # screenshot
# result = requests.get("http://localhost:12000/screenshot")
# print(result.content.decode())

# télécharger un fichier
response = requests.get("http://localhost:12000/get_current_dir")
data = json.loads(response.content)
dir = data[0]
filenames = json.loads(data[1]) # devra recevoir un filename
file_path = json.dumps("\\".join((dir, str(filenames[1])))) 
result = requests.get("http://localhost:12000/download", data=file_path)  # devra recevoir un file path 
print()
print(result.content.decode("utf-8"))


# # aller dans un dossier
# response = requests.get("http://localhost:12000/get_current_dir")
# data = json.loads(response.content)
# dir = data[0]
# filenames = json.loads(data[1]) 
# result = requests.get("http://localhost:12000/go_dir", data=filenames[0])
# print()
# print(result.content.decode("utf-8"))