import requests
import json


class SparkBot:
    
    def __init__(self, access_token):
        requests.packages.urllib3.disable_warnings()
        
        # this is it
        # url and the parameters
        self.url = "https://api.ciscospark.com/v1"
        self.bot_token = access_token
        self.access_token = "Bearer " + access_token
        self.message_data = None
        
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
        
    # return more data a specific message with id <message_id> 
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
    
    # this is a decorator where you will write your function that you want to be mapped to a specific function, f
    # This function happens when a message, let's say 'hi' is heard
    def onHears(self, message_text):
        def decorator(f):
            self.hears_to_function[message_text] = f
        return decorator
    
    
    # this function is meant to receive messages from the flask webhook listener
    # it will then map this message to the respective function depending on the self.hears_to_function dictionary
    # the respective function is finally carried out
    # for instance, if the mapping is {'hi': hi_function}, and 'hi' is the message, the hi_function will be executed
    def receiveMessage(self, message, roomId):
        if message in self.hears_to_function:
            message_function = self.hears_to_function[message]
            message_function()
    
    # this function allows for a bot to be able to send a file
    # once someone has created a bot object, this can be called and a file will be sent to a user
    def send_attachment(self, room_id, files_path):
        api_call = "/messages"
        url = self.url + api_call
        headers = {
            "Content-Type": "application/json",
            "authorization": self.access_token
        }
        # response = requests.post(url, json={"roomId":room_id, "text":message}, headers=headers)
        response = requests.post(url, json={"roomId":room_id, "files":files_path}, headers=headers)
        print(response.text)
        return None


    def messageNotUnderstood(self):
        self.sendMessage(self.message_data["roomId"], "Sorry, could not understand what you said")
        return None
        # print(type(self.message_data))
    
