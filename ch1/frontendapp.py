import requests
import json

URL = "http://127.0.0.1:8000/stucre/"

data = {
    'name':'geek4',
    'roll':4
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

print(r.json())