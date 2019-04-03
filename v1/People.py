import sys 
import requests


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
        data = requests.get( self.URL + url_route, headers=self.headers, params=params)
        return data
    
    def get_person_details(self, personId=None):
        """
        returns specific information of the person with ID personId
        uses https://api.ciscospark.com/people/{ personId } - GET request
        API reference can be found in: https://developer.webex.com/docs/api/v1/people/get-person-details 
        """

        if personId ==  None:
            sys.exit("'personId' is a required field")
        
        url_route = "people"

        data = requests.get( self.URL + url_route + "/" + personId, headers=self.headers )
        return data
        
    
    def get_own_details(self):
        """
        gets the bots own information
        uses https://api.ciscospark.com/people - GET request
        API reference can be found in: https://developer.webex.com/docs/api/v1/people/get-my-own-details 
        """

        url_route = "people/me"

        data = requests.get( self.URL + url_route, headers=self.headers )
        return data

