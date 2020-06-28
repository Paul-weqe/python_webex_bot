from python_webex.webhook.handlers import MessageReceivingHandler, AttachmentReceivingHandler 
from flask import Flask, request
import inspect


app = Flask(__name__)
bot = None


@app.route("/", methods=[ 'GET', 'POST' ])
def index():
    json_data = request.get_json()
    message_id = json_data[ "data" ][ "id" ]
    message_info = bot.get_message_details( message_id=message_id ).json()

    handler = MessageReceivingHandler(bot, message_info)
    handler.handle_message()    
    response = "incoming message handled"
    return response

@app.route("/attachment-response", methods=["GET", "POST"])
def attachment_response():
    json_data = request.get_json()
    message_id = json_data['data']['messageId']
    message_info = bot.get_attachment_response(json_data['data']['id'])

    handler = AttachmentReceivingHandler(bot, message_info, message_id)
    handler.handle_attachment()

    response = "incoming attachment handled"
    return response
