import requests
import json

active_bot = None

class SparkBot:
    
    def __init__(self, access_token):
        requests.packages.urllib3.disable_warnings()
        
        
        # url and the parameters
        self.url = "https://api.ciscospark.com/v1"
        self.bot_token = access_token
        self.access_token = "Bearer " + access_token
        
        
        # this dictionary holds what will be heard to the corresponding function that the user will keep
        # for example, if you hear 'hi', and the corresponding function to handle this message is hi_function()
        # this will be stored as { 'hi': hi_function }
        self.hears_to_function = {
            
        }
        
        return None
    
    # send message to a specific party
    def sendMessage(self, room_id, message):
        api_call = "/messages"
        url = self.url + api_call
        headers = {
            "Content-Type": "application/json",
            "authorization": self.access_token
        }
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
        
        # looks if there are any errors in getting the message and gives back the output
        dict_response = json.loads(response.text)
        if "error" in dict_response:
            return False
        return dict_response
    
    def onHears(self, message):
        def decorator(f):
            self.hears_to_function[message] = f
        return decorator
    
    
    # this function is meant to receive messages from the flask webhook listener
    # it will then map this message to the respective function depending on the self.hears_to_function dictionary
    # the respective function is finally carried out
    # for instance, if the mapping is {'hi': hi_function}, and 'hi' is the message, the hi_function will be executed
    def receiveMessage(self, message, roomId):
        if message in self.hears_to_function:
            message_function = self.hears_to_function[message]
            message_function()
        return None
    
    
