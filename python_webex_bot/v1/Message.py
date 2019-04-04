import requests 
import sys

class Message:

    # Message requests uses URL https://api.ciscospark.com/v1/messages
    
    def send_message(self, roomId=None, text=None, files=[]):
        """
        Allows for one to send a message to a room
        details on the rooms URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/create-a-message
        'files' is a list of the files(images, audios etc) you want to send to the user
        """

        if roomId == None:
            sys.exit("'roomId' is a required field")
        
        if text == None:
            sys.exit("'text' is a required field")

        if type(files) != list:
            sys.exit("'files' needs to be a list")

        url_route = "messages"


        data = {
            "roomId": roomId,
            "text": text,
        }

        if len(files) > 0:
            data["files"] = files
        
        data = requests.post( self.URL + url_route, headers=self.headers, json=data )
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
        data = requests.get( self.URL + url_route, headers=self.headers, params=params )
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
        data = requests.get( self.URL + url_route + "/direct", headers=self.headers, params=params )
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

        data = requests.get( self.URL + url_route, headers=self.headers)
        return data

    def delete_message(self, messageId=None):
        """
        deletes a message with ID messageId
        details on the delete message URL can be found in https://developer.webex.com/docs/api/v1/messages/delete-a-message
        """

        if messageId == None:
            sys.exit("'messageId' is not a required field")
        
        url_route = "messages/" + messageId

        data = requests.delete( self.URL + url_route, headers=self.headers )
        return data
