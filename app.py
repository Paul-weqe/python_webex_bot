from flask import Flask, request
import spark
import requests
import json
import test

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    return "Cool"


# this webhook is meant to listen to anything on messages side of the webhook
# ranging from attached files to actual text messages
@app.route("/messages", methods=["POST"])
def messages():
    data = request.get_json()
    bot = test.active_bot
    
    # 
    message_id = data['data']['id']
    url = "https://api.ciscospark.com/v1/messages/" + message_id
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer " + bot.bot_token
    }

    # 
    response = requests.get(url, headers=headers)
    # print(response.text)
    message_json = json.loads(response.text)

    # we get the json from the data that has been sent as a dictionary
    bot.message_data = message_json

    # what happens if the message is a mention
    if ("mentionedPeople" in message_json) and (message_json["roomType"] == "group"):
        message_json["text"] = message_json["text"].replace("random ", "")
        bot.receiveMention( message_json["text"], message_json["roomId"] )

    # what happens if the message is a direct text
    elif ( "text" in message_json ):
        bot.receiveMessage( message_json["text"], message_json["roomId"] )
    
    return "Message"


if __name__ == "__main__":
    app.run(debug=True)




