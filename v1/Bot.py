from v1.People import People
from v1.Room import Room
from v1.Webhook import Webhook
from v1.Message import Message



class Bot(People, Room, Webhook, Message):

    def __init__(self):

        # self.hears to function maps when a specific word is heard to a function
        # for example, when one says 'hi' and you want to map it to say_hi() function
        self.hears_to_function = {
            
        }

    """
    decorator meant to do a specific action when called
    """
    def on_hears(self, message_text):
        def hear_decorator(f):
            self.hears_to_function[message_text] = f
        
        return hear_decorator
    
    
    



