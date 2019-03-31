import requests
import sys
import os 

URL = "https://api.ciscospark.com/"
auth_token = os.getenv("auth_token")

if auth_token == None:
    sys.exit("'auth_token' not set in environment variables")

headers = {
    "Authorization": "Bearer " + auth_token,
    "Content-Type": "application/json"
}

class Webhook:

    def list_all_wekhooks(self):
        """
        GETS A LIST OF ALL THE WEBHOOKS CURRENTLY CONNECTED TO YOUR BOT
        uses the https://api.ciscospark.com/v1/webhooks - GET request
        details on the list webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/list-webhooks
        """

        url_route = "webhooks"

        data = requests.get(URL + url_route, headers=headers)

        return data
    
    def create_webhook(self, name=None, targetUrl=None, resource=None, event=None):
        """
        Enables one to create a webhook that will be listening to events sent to the bot
        uses the https://api.ciscospark.com/v1/webhooks - POST request
        details on create webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook
        """

        url_route = "webhooks"

        if name == None:
            sys.exit("'name' is a required field")
        
        elif targetUrl == None:
            sys.exit("'targetUrl' is a required field")
        
        elif resource == None:
            sys.exit("'resource' is a required field")
        
        elif event == None:
            sys.exit("'event' is a required field")

        json = {
            "name": name, "targetUrl": targetUrl, "resource": resource, "event": event
        }

        data = requests.post(URL + url_route, headers=headers, json=json)
        return data
    
    def delete_webhook(self, webhookId=None):
        """
        Deletes a webhook that has ID webhookId
        uses the https://api.ciscospark.com/webhooks - DELETE request
        details on delete webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/delete-a-webhook 
        """

        url_route = "webhooks"

        if webhookId == None:
            sys.exit("'webhookId' is a required field")
        
        data = requests.delete(URL + url_route + "/" + webhookId, headers=headers)
        return data
    
    def update_webhook(self, webhookId=None, name=None, targetUrl=None):
        """
        'name' is the updated name of the webhook
        'targetUrl' is the updated targetUrl of the webhook

        Edit a webhook with ID of webhookId
        uses the https://api.ciscospark.com/webhooks - PUT request
        details on edit webhook URL can be found in https://developer.webex.com/docs/api/v1/webhooks/update-a-webhook
        """

        url_route = "webhooks"

        if webhookId == None:
            sys.exit("'webhookId' is a required field")
        
        elif name == None:
            sys.exit("'name' is a required field")
        
        elif targetUrl == None:
            sys.exit("'targetUrl' is a required field")
        
        json = {
            "name": name, "targetUrl": targetUrl
        }

        data = requests.put( URL + url_route + "/" + webhookId, json=json, headers=headers )
        return data
    
    def get_webhook_details(self, webhookId=None):
        """
        Get the details of a single webhook with id of webhookId
        uses https://api.ciscospark.com/webhooks/{roomId} - GET request
        details on get webhook details URL can be found in https://developer.webex.com/docs/api/v1/webhooks/get-webhook-details 
        """

        url_route = "webhooks"

        if webhookId == None:
            sys.exit("'webhookId' is a required field")
        
        data = requests.get(URL + url_route, headers=headers)
        return data
