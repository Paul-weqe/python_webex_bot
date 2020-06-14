from python_webex.v1.Card import Card
import requests 
import sys

class Message:
    """
    Message requests uses URL https://api.ciscospark.com/v1/messages

    Enables us to interact with the Messages in the Cisco Webex platform. 
    sending messages, listing your messages etc.  
    """
    
    def send_message(self, room_id=None, text=None, files=[]):
        """
        Allows for one to send a message to a room
        details on the rooms URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/create-a-message
        'files' is a list of the files(images, audios etc) you want to send to the user, if the user wants to attach files with the message
        
        ----
        Arguments
        @ room_id: string => This is the ID of the room you are sending the message to 
        @ text: string => The text being sent in the message 
        @ files: list of string =>  A list of files you want to sell. Each element in the list is a directory path to the file.
                                    e.g files=['/this/is/my/path/this_image.jpg', 'this/is/my/second/path/this_pdf.pdf']
        """
        if room_id == None:
            sys.exit("'roomId' is a required field")
        
        if text == None:
            sys.exit("'text' is a required field")

        if type(files) != list:
            sys.exit("'files' needs to be a list")

        url_route = "messages"

        data = {
            "roomId": room_id,
            "text": text,
        }

        if len(files) > 0:
            data["files"] = files
        
        data = requests.post( self.URL + url_route, headers=self.headers, json=data )
        return data
    
    def send_card(self, card:Card,  room_id:str, markdown: str="[This is the default markdown title]"):
        """
		Cars are elements that can hold forms and improve interactivity of the messages. 
        For example, if you are using a bot to monitor your networking devices, this will require you to login the networking devices first. 
        You can send a form for one to login to the networking devices. 
        """
        
        message = {
            "roomId": room_id,
            "markdown": markdown,
            "attachments": card.content
        }
        
        url_route = "messages"
        data = requests.post(self.URL + url_route, headers=self.headers, json=message)
        return data
    
    def get_attachment_response(self, attachment_id: str):
        """
        Gets the response for when an attachment has been sent
        """
        url_route = "attachment/actions/{}".format(attachment_id)

        response = requests.get(self.URL + url_route, headers=self.headers)
        return response.json()

    def get_messages(self, room_id=None):
        """
        gets all the messages sent and received in a specific room
        details on the list-messages URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/list-messages
        """

        if room_id == None:
            sys.exit("'room_id' is a required field")
        
        url_route = "messages"

        params = {
            "roomId": room_id
        }
        data = requests.get( self.URL + url_route, headers=self.headers, params=params )
        return data
    
    def get_direct_messages(self, person_id=None):
        """
        gets a list of all the messages sent in 1 to 1 rooms. This is basically a list all the DMs :)
        details on the list-direct-messages URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/list-direct-messages 
        """
        
        if person_id == None:
            sys.exit("'person_id' is a mandatory field")

        url_route = "messages"

        params = {
            "personId": person_id
        }
        data = requests.get( self.URL + url_route + "/direct", headers=self.headers, params=params )
        return data
    
    def get_message_details(self, message_id=None):
        """
        gets details of a specific message
        e.g roomId, roomType, created, mentionedPeople ...
        details on the get message details URL parameters can be found in https://developer.webex.com/docs/api/v1/messages/get-message-details
        """

        if message_id == None:
            sys.exit("'message_id' is a required field")
        
        url_route = "messages/" + message_id

        data = requests.get( self.URL + url_route, headers=self.headers)
        return data

    def delete_message(self, message_id=None):
        """
        deletes a message with ID messageId
        details on the delete message URL can be found in https://developer.webex.com/docs/api/v1/messages/delete-a-message
        """

        if message_id == None:
            sys.exit("'message_id' is not a required field")
        
        url_route = "messages/" + message_id

        data = requests.delete( self.URL + url_route, headers=self.headers )
        return data
