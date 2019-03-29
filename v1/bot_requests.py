"""
"""

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


class Room:

    def list_all_rooms(self):
        """
        Gives a list of all the rooms the specific bot is in
        this request uses url https://api.ciscospark.com/rooms 
        details on the rooms URL can be found in: https://developer.webex.com/docs/api/v1/rooms/list-rooms
        """
        url_route = "rooms"
        data = requests.get( URL + url_route, headers=headers)
        return data
    
    def create_room( self, title=None, teamId=None, room_type=None ):
        """
        Creates a room within a team, also known as a space. This will be within the team with ID teamId
        this request uses url https://api.ciscospark.com - POST request
        details on the create rooms can be found in https://developer.webex.com/docs/api/v1/rooms/create-a-room 
        """

        if title == None:
            sys.exit("'title' is a required field")
        
        if teamId == None:
            sys.exit("'teamId; is a required field")

        url_route = "rooms"

        json = {
            "teamId": teamId,
            "title": title
        }

        if room_type != None:
            json["type"] = room_type

        data = requests.post( URL+url_route, json=json, headers=headers)
        return data

    def get_room_details(self, roomId=None):
        """
        GETS DETAILS OF A PARTICULAR ROOM
        request uses url https://api.ciscospark.com/{roomId} - GET request
        details on the get room details can be found in https://developer.webex.com/docs/api/v1/rooms/get-room-details 
        """

        if roomId == None:
            sys.exit("'roomId' is a required field")
        
        url_route="rooms"

        data = requests.get( URL+url_route+"/"+roomId, headers=headers )
        return data

    def update_room_details(self, roomId=None, title=None):
        """
        UDPATES THE DETAILS OF A PARTICULAR ROOM based on the **kwargs given by the user
        request uses url https://api.ciscospark.com/{roomId} - PUT request
        details on the update room details can be found in https://developer.webex.com/docs/api/v1/rooms/update-a-room
        """

        if roomId is None:
            sys.exit("'roomId' is a required field")
        
        elif title is None:
            sys.exit("'title' is a required field")
        
        json = {
            "title": title
        }

        url_route = "rooms"

        data = requests.put( URL + url_route + '/' + roomId,  json=json, headers=headers)
        return data
    
    def delete_room(self, roomId=None):
        """
        DELETES A ROOM with ID roomId
        uses url https://api.ciscospark.com/v1/rooms/{roomId}
        details on the delete room can be found in https://developer.webex.com/docs/api/v1/rooms/delete-a-room
        """

        if roomId is None:
            sys.exit("'roomId' is a required field")
        
        url_route = "rooms"
        data = requests.delete( URL + url_route + "/" +roomId, headers=headers )
        return data

class Message:

    # Message requests uses URL https://api.ciscospark.com/v1/messages
    
    def send_message(self, roomId=None, text=None):
        """
        Allows for one to send a message to a room
        details on the rooms URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/create-a-message
        """

        if roomId == None:
            sys.exit("'roomId' is a required field")
        
        if text == None:
            sys.exit("'text' is a required field")

        url_route = "messages"

        data = {
            "roomId": roomId,
            "text": text,
        }
        
        data = requests.post( URL + url_route, headers=headers, json=data )
        return data

    def list_messages(self, roomId=None):
        """
        gets all the messages sent and received in a specific room
        details on the list-messages URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/list-messages
        """

        if roomId == None:
            sys.exit("'roomId' is a required field")
        
        url_route = "messages"

        params = {
            "roomId": roomId
        }
        data = requests.get( URL + url_route, headers=headers, params=params )
        return data
    
    def list_direct_messages(self, personId=None):
        """
        gets a list of all the messages sent in 1 to 1 rooms. This is basically a list all the DMs :)
        details on the list-direct-messages URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/list-direct-messages 
        """
        
        if personId == None:
            sys.exit("'personId' is a mandatory field")

        url_route = "messages"

        params = {
            "personId": personId
        }
        data = requests.get( URL + url_route + "/direct", headers=headers, params=params )
        return data
    
    def get_message_details(self, messageId=None):
        """
        gets details of a specific message
        e.g roomId, roomType, created, mentionedPeople ...
        details on the get message details URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/get-message-details
        """

        if messageId == None:
            sys.exit("'messageId' is a required field")
        
        url_route = "messages/" + messageId

        data = requests.get( URL + url_route, headers=headers)
        return data

    def delete_message(self, messageId=None):
        """
        deletes a message with ID messageId
        details on the delete message URL can be found in https://developer.webex.com/docs/api/v1/messages/delete-a-message
        """

        if messageId == None:
            sys.exit("'messageId' is not a required field")
        
        url_route = "messages/" + messageId

        data = requests.delete( URL + url_route, headers=headers )
        return data

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


class People:

    def list_people(self, email=None):
        """
        gets a list of people with a particular attribute
        uses https://api.ciscospark.com/people - GET request
        """

        if email == None:
            sys.exit("'email' is a required field")

        url_route = "people"

        params = {
            "email": email
        }
        data = requests.get( URL + url_route, headers=headers, params=params)
        return data
    
    def get_person_details(self, personId=None):
        """
        """

        if personId ==  None:
            sys.exit("'personId' is a required field")
        
        url_route = "people"

        data = requests.get( URL + url_route + "/" + personId, headers=headers )
        return data

    
    def get_own_details(self):
        """
        """

        url_route = "people"

        data = requests.get(URL + url_route + "/people/me", headers=headers)
        return data

people = People()
print(
    people.get_own_details().json()
)
