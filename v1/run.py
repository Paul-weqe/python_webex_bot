import requests
import os

headers = {
    "Authorization": "Bearer "+os.getenv("auth_token")
}


URL = "https://api.ciscospark.com/v1/rooms"

data = requests.get(URL, headers=headers)
print(data.json())