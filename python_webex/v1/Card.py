import sys
import requests


"""
Cards give a better level of interactivity to the Webex Platform. 
They can allow us to create form like interactive interfaces from the bot.
"""

class Card:
    def __init__(self):
        self.content = [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                        {
                            "type": "ColumnSet",
                            "columns": [
                                {
                                    "type": "Column",
                                    "width": 3,
                                    "items": []
                                }]
                        }
                    ],
                    "actions": [
                    ]
                }
            }
        ]

    def __add_element(self, element_dict):
        self.content[0]["content"]["body"][0]["columns"][0]["items"].append(element_dict)
    
    def __add_action(self, action_dict):
        self.content[0]["content"]["actions"].append(action_dict)
    
    def get_all_input_ids(self):
        inputs = []
        items = self.content[0]["content"]["body"][0]["columns"][0]["items"]
        for item in items:
            if "id" in item.keys():
                inputs.append(item["id"])
        return inputs
    
    def check_if_id_exists(self, id):
        ids = self.get_all_input_ids()
        items = self.content[0]["content"]["body"][0]["columns"][0]["items"]
        if id in ids:
            for item in items:
                if item['id'] == id:
                    items.remove(item)
    
    def check_if_submit_button_exists(self):
        actions = self.content[0]["content"]["actions"]
        for action in actions:
            if action["type"] == "Action.Submit":
                actions.remove(action)
    

    """
    Textblock is essentially normal text in html. as how you would put a <p>Here is the text</p>
    The TextBlock attributes and their explanations can be found at: https://adaptivecards.io/schemas/adaptive-card.json#/definitions/TextBlock
    """
    def add_text_block(
        self, text: str, is_subtle: bool = False, size: str = "default", weight: str = "default", wrap: bool = False
    ):
        element = {
            "type": "TextBlock",
            "text": text,
            "isSubtle": is_subtle,
            "size": size,
            "weight": weight,
            "wrap": wrap
        }
        self.__add_element(element)

    
    """
    add_input_text() adds the traditional text fields as they are used in normal forms. interprated as <input type="text"> when it comes to html
    The various attribute values can be found at: https://adaptivecards.io/schemas/adaptive-card.json#/definitions/Input.Text 
    Have a look at the URL above for more details on how the field is used
    """
    def add_input_text(
        self, input_id:str, input_is_multiline:bool = False, input_max_length:int = None, input_placeholder: str = None, input_value: str = None
    ):
        self.check_if_id_exists(input_id)
        element = {
            "id": input_id,
            "type": "Input.Text",
            "isMultiline": input_is_multiline
        }

        if input_max_length is not None: element["maxLength"] = input_max_length 
        if input_placeholder is not None: element["placeholder"] = input_placeholder 
        if input_value is not None: element["value"] = input_value 
        self.__add_element(element)
    
    """
    add_submit_action_btn() adds the button that submits the 'form' that has been sent as a message. Works like the <input type="submit"> element in html. 
    """
    def add_submit_action_btn(
        self, title: str = "submit"
    ):
        self.check_if_submit_button_exists()
        action = {
            "type": "Action.Submit",
            "title": title
        }
        self.__add_action(action)

    
    """
    The various attribute values can be found at: https://adaptivecards.io/schemas/adaptive-card.json#/definitions/Input.ChoiceSet
    """
    def add_input_choiceset(
        self, input_id: str, input_choices:list=[], input_is_multiselect: bool = False, input_value:str = None
    ):
        self.check_if_id_exists(input_id)
        element = {
            "id": input_id,
            "type": "Input.ChoiceSet",
            "choices": input_choices,
            "isMultiSelect": input_is_multiselect
        }

        if input_value is not None: element["value"] = input_value
        self.__add_element(element)
