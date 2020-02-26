from flask import Flask, request
from pprint import pprint

app = Flask(__name__)
bot = None

@app.route("/", methods=[ 'GET', 'POST' ])
def index():

    json_data = request.get_json()
    
    message_id = json_data[ "data" ][ "id" ]
    message_info = bot.get_message_details( message_id=message_id ).json()

    if message_info[ "personId" ] == bot.get_own_details().json()[ 'id' ]:
        return "cannot respond to my own messages"

    if message_info[ "text" ].strip() != "" and message_info[ "text" ] in bot.hears_to_function:
        message_text = message_info[ "text" ]
        bot.hears_to_function[ message_text ]( room_id=message_info["roomId"] )
        
    elif message_info["text"].strip() != "" and  message_info[ "text" ] not in bot.hears_to_function:
        bot.hears_to_function[ "*" ]( room_id=message_info["roomId"] )

    return "successfully responded"

@app.route("/attachment-response", methods=["GET", "POST"])
def attachment_response():
    print(request)
    json_data = request.get_json()
    message_id = json_data['data']['messageId']
    message_dict = bot.get_attachment_response(json_data['data']['id'])

    response = bot.attachment_response_to_function[message_id](message_dict)
    

    return "attachment response received"
