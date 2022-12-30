import requests
import json

headers = {'accept': 'application/json', 'auth_key': '0da0bda4098cda9b8edd577428a3df1210a11cfbffd2f0be4c5aa05b',
           'Content-Type': 'multipart/form-data'}
ID = '5ef87cf9-e21d-42ee-92f0-61ed1596c2e0'

info = {"name": "cat", "animal_type": "buldog", "age": "2"}


resput = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{ID}", headers=headers, data=json.dumps(info, ensure_ascii=False))
print(resput.text)
resdelete = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/{info}", headers=headers)
