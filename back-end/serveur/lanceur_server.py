
import requests

# obtenir le repertoire courant
result = requests.get("http://localhost:12000/get_current_dir")
print(result.content.decode())

# # aller en arrière
# result = requests.get("http://localhost:12000/go_back")
# print(result.content.decode())

# # screenshot
# result = requests.get("http://localhost:12000/screenshot")
# print(result.content.decode())

# # télécharger un fichier
# result = requests.get("http://localhost:12000/get_current_dir")
# print(result.content.decode())