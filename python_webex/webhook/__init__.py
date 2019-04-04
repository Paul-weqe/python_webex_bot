from flask import Flask, request

app = Flask(__name__)
bot = None

@app.route("/", methods=[ 'GET', 'POST' ])
def index():

    json_data = request.get_json()
    
    message_id = json_data[ "data" ][ "id" ]
    message_info = bot.get_message_details( message_id=message_id ).json()

    print(message_info)
    
    if message_info[ "personId" ] == bot.get_own_details().json()[ 'id' ]:
        return "cannot respond to my own messages"

    if message_info[ "text" ].strip() != "" and message_info[ "text" ] in bot.hears_to_function:
        message_text = message_info[ "text" ]
        bot.hears_to_function[ message_text ]( room_id=message_info["roomId"] )
        
    elif message_info["text"].strip() != "" and  message_info[ "text" ] not in bot.hears_to_function:
        bot.hears_to_function[ "*" ]( room_id=message_info["roomId"] )
    
    return "successfully responded"



