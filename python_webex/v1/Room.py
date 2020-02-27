import requests
import sys


class Room:

    def get_all_rooms(self):
        """
        Gives a list of all the rooms the specific bot is in
        this request uses url https://api.ciscospark.com/rooms 
        details on the rooms URL can be found in: https://developer.webex.com/docs/api/v1/rooms/list-rooms
        """
        url_route = "rooms"
        data = requests.get(self.URL + url_route, headers=self.headers)
        return data

    def create_room(self, title=None, team_id=None, room_type=None):
        """
        Creates a room within a team, also known as a space. This will be within the team with ID teamId
        this request uses url https://api.ciscospark.com - POST request
        details on the create rooms can be found in https://developer.webex.com/docs/api/v1/rooms/create-a-room 
        """

        if title is None:
            sys.exit("'title' is a required field")
    
        if team_id is None:
            sys.exit("'teamId; is a required field")

        url_route = "rooms"

        json = {
            "teamId": team_id,
            "title": title
        }

        if room_type is not None:
            json["type"] = room_type

        data = requests.post(self.URL + url_route, json=json, headers=self.headers)
        return data

    def get_room_details(self, room_id=None):
        """
        GETS DETAILS OF A PARTICULAR ROOM
        request uses url https://api.ciscospark.com/{roomId} - GET request
        details on the get room details can be found in https://developer.webex.com/docs/api/v1/rooms/get-room-details 
        """

        if room_id is None:
            sys.exit("'roomId' is a required field")

        url_route = "rooms"

        data = requests.get(self.URL + url_route + "/" + room_id, headers=self.headers)
        return data

    def update_room_details(self, room_id=None, title=None):
        """
        UDPATES THE DETAILS OF A PARTICULAR ROOM based on the **kwargs given by the user
        request uses url https://api.ciscospark.com/{roomId} - PUT request
        details on the update room details can be found in https://developer.webex.com/docs/api/v1/rooms/update-a-room
        """

        if room_id is None:
            sys.exit("'roomId' is a required field")

        elif title is None:
            sys.exit("'title' is a required field")

        json = {
            "title": title
        }

        url_route = "rooms"

        data = requests.put(self.URL + url_route + '/' + room_id, json=json, headers=self.headers)
        return data

    def delete_room(self, room_id=None):
        """
        DELETES A ROOM with ID roomId
        uses url https://api.ciscospark.com/v1/rooms/{roomId}
        details on the delete room can be found in https://developer.webex.com/docs/api/v1/rooms/delete-a-room
        """

        if room_id is None:
            sys.exit("'roomId' is a required field")

        url_route = "rooms"
        data = requests.delete(self.URL + url_route + "/" + room_id, headers=self.headers)
        return data




