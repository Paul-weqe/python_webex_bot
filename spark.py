import requests
import json

class Spark:
    
    def __init__(self, access_token):
        requests.packages.urllib3.disable_warnings()
        # url and the parameters
        self.url = "https://api.ciscospark.com/v1"
        self.access_token = "Bearer " + access_token
        
        return None
    
    # send message to a specific party
    def sendMessage(self, room_id, message):
        api_call = "/messages"
        url = self.url + api_call
        headers = {
            "Content-Type": "application/json",
            "authorization": self.access_token
        }
        json = message
        response = requests.post(url, json={"roomId":room_id, "text":message}, headers=headers)
        print(response.text)
        return None
    
    def getMessageDetails(self, message_id):
        api_call = "/messages"
        url = self.url + api_call + "/" + message_id
        print(url)
        headers = {
            "Content-Type": "application/json",
            "authorization": self.access_token
        }
        response = requests.get(url, headers=headers)
        print(response.text)
        return None
    