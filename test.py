import requests 
import json 


url = 'http://ip-api.com/batch'

# ip = "185.195.59.38"

data =  [
        "185.195.59.38"
    ]

res = requests.post(url, json=data)

res_data = json.dumps(res.json())

json_data = json.loads(res_data)

print(json_data)
print(json_data[0]["status"])

# print(json_data["status"])