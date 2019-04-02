from flask import Flask, request

app = Flask(__name__)
bot = None

@app.route("/", methods=[ 'GET', 'POST' ])
def index():

    json_data = request.get_json()
    
    message_id = json_data[ "data" ][ "id" ]
    message_info = bot.get_message_details( messageId=message_id ).json()
    print(message_info)
    
    if message_info[ "personId" ] == bot.get_own_details().json()[ 'id' ]:
        return "cannot respond to my own messages"
    
    message_text = message_info[ "text" ]
    bot.hears_to_function[ message_text ]( room_id=message_info["roomId"] )
    
    return "successfully responded"

