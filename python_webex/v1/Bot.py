from python_webex.v1.People import People
from python_webex.v1.Room import Room
from python_webex.v1.Webhook import Webhook
from python_webex.v1.Message import Message

import os
import sys


class Bot(People, Room, Webhook, Message):

    def __init__(self):

        # declare headers and how the token will be gotten from the system
        self.URL = "https://api.ciscospark.com/"
        self.auth_token = os.getenv("auth_token")

        if self.auth_token == None:
            sys.exit("'auth_token' not set in the environment variables")
        
        self.headers = {
            "Authorization": "Bearer " + self.auth_token,
            "Content-Type": "application/json"
        }
        
        # self.hears to function maps when a specific word is heard to a function
        # for example, when one says 'hi' and you want to map it to say_hi() function
        self.hears_to_function = {

        }

        self.hears_file_to_function = {
            
        }

        self.attachment_response_to_function = {

        }

        # default attachment variable will hold the function that is supposed to be the default action whenever an attachment is sent to the bot
        self.default_attachment = None

        # maps what will happen when a file is received with a particular type of text
        self.hears_file_to_function = {

        }

        self.attach_function = None

    """
    decorator meant to do a specific action when called
    """
    def on_hears(self, message_text):
        def hear_decorator(f):
            self.hears_to_function[message_text] = f
        return hear_decorator
    
    """
    decorator waiting for any attachment that has been sent to the bot
    """
    def set_default_file_response(self):
        def hear_default_file_attachment(f):
            self.default_attachment = f
        return hear_default_file_attachment
    
    """
    decorator for when a file is received with a particular type of text. 
    """
    def set_file_action(self, message_text: str):
        def hear_file_attachment(f):
            self.hears_file_to_function[message_text] = f
        return hear_file_attachment

    """
    decorator waiting for an attachment to be filled and returned for it to do a specific action
    """
    def attachment_response(self, message_id: str):
        def response_decorator(f):
            self.attachment_response_to_function[message_id] = f
        return response_decorator
