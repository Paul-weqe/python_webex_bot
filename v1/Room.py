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

