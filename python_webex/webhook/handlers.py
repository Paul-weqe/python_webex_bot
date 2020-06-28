"""Explanation of the route handlers


This module takes care of handling logic of data from the '@app.route's  in the webhook/__init__.py file
webhook/__init__.py file mainly deals with getting requests and messages from the sender,
while this route_handlers.py mainly deals with the logic after receiving this information. 
This mainly has to do with cleaning up the webhook/__init__.py which was rather messy. 

Attributes:
    # Bot below refers to Bot class from python_webex.v1.Bot
    - bot(Bot): an instance of the bot that we are dealing with when running our program. 
    - message_info(dictionary): a dictionary of all the details that were gotten from the message sent. 
        For more information, you can have a look at the 

Todo: 
    *
"""
from python_webex.v1.Bot import Bot


class MessageReceivingHandler:

    def __init__(self, bot, message_info):
        self.bot = bot
        self.message_info = message_info

    def handle_message(self):
        # looks for in case there was a file(image, document etc) attached in the message. 
        if 'files' in self.message_info:
            self.handle_messages_with_files()
            return None
        
        # handles when a normal message is sent with text in the message
        # and a way to handle the text received has been defined by the bot programmer. 
        elif self.message_info[ "text" ].strip() != "" and self.message_info[ "text" ] in self.bot.hears_to_function:
            self.handle_messages_without_file_and_with_text()
            return None

        # handles when a normal message is sent with text in the message
        # but a way to handle the text received has not been defined by the bot programmer
        elif self.message_info["text"].strip() != "" and  self.message_info[ "text" ] not in self.bot.hears_to_function:
            self.handle_messages_without_file_and_without_text()
            return None

    # function handles when messages are sent with file attachments (images, documents etc)
    def handle_messages_with_files(self):
        
        # loop for when the file attached(image, document..etc) is sent with a text accomanied. 
        # for example, if an image is sent with caption "Felt cure, might delete later"
        # this is considered a file attachment with a text alongside
        if "text" in self.message_info:
            self.handle_messages_with_file_and_text()
        
        elif self.bot.default_attachment is not None:
            self.handle_messages_with_files_and_without_text_and_with_default_attachment_set()
            
        else:
            self.handle_messages_without_file_and_without_text()

    def handle_messages_with_file_and_text(self):
        message_text = self.message_info["text"]

        if self.message_info['text'] in self.bot.hears_file_to_function:

            # handles when the bot has been programmed to handle messages with files
            # and the specific text that is being sent to the bot. 
            # looks for if the function has message_info specified; and this is used in mapping of
            # the message information
            if 'message_info' in self.bot.hears_file_to_function[message_text].__code__.co_varnames:
                self.bot.hears_file_to_function[message_text](
                    files = self.message_info['files'], 
                    room_id = self.message_info['roomId'], 
                    message_info = self.message_info
                )
            
            else:
                self.bot.hears_file_to_function[message_text](
                    files = self.message_info['files'], 
                    room_id = self.message_info['roomId']
                )
                
        
        elif "*" in self.bot.hears_file_to_function:
            
            if 'message_info' in self.bot.hears_to_function["*"].__code__.co_varnames:
                self.bot.hears_file_to_function["*"](
                    files = self.message_info["files"],
                    room_id = self.message_info['roomId'],
                    message_info = self.message_info
                )
                
            else:
                self.bot.hears_file_to_function["*"](
                    files = self.message_info["files"],
                    room_id = self.message_info["roomId"]
                )

        else:
            return "Default response for file sent with text not set"

    def handle_messages_without_file_and_with_text(self):
        message_text = self.message_info["text"]

        if 'message_info' in self.bot.hears_to_function[message_text].__code__.co_varnames:
            self.bot.hears_to_function[message_text](
                room_id = self.message_info["roomId"], 
                message_info = self.message_info
                )
        
        else:
            self.bot.hears_to_function[message_text](room_id=self.message_info["roomId"])
    
    def handle_messages_without_file_and_without_text(self):
        if 'message_info' in self.bot.hears_to_function["*"].__code__.co_varnames:
            self.bot.hears_to_function["*"](
                room_id = self.message_info["roomId"], 
                message_info = self.message_info
            )
        else:
            self.bot.hears_to_function["*"](
                room_id=self.message_info["roomId"]
            )
    
    def handle_messages_with_files_and_without_text_and_with_default_attachment_set(self):
        if 'message_info' in self.bot.default_attachment.__code__.co_varnames:
            self.bot.default_attachment(
                files = self.message_info['files'], 
                room_id = self.message_info['roomId'], 
                message_info = self.message_info
            )

        else:
            self.bot.default_attachment(
                files = self.message_info['files'], 
                room_id = self.message_info['roomId']
                )

class AttachmentReceivingHandler:
    
    def __init__(self, bot, message_info, message_id):
        self.bot = bot
        self.message_info = message_info
        self.message_id = message_id
    
    def handle_attachment(self):
        if self.message_id in self.bot.attachment_response_to_function:
            self.handle_response_of_known_attachment()
        else:
            self.handle_default_response_for_attachments()
    
    def handle_response_of_known_attachment(self):
        response = self.bot.attachment_response_to_function[self.message_id](self.message_info)

    def handle_default_response_for_attachments(self):
        room_id = self.message_info["roomId"]
        self.bot.send_message(
            room_id=room_id, 
            text="The bot has not been configured to handle this form's submission. Be patient"
        )
