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
    # print(type(response.text))
    message_json = json.loads(response.text)

    # print( message_json["text"])
    bot.message_data = message_json
    if "text" in message_json:
        bot.receiveMessage( message_json["text"], message_json["roomId"] )
    
    return "Message"


if __name__ == "__main__":
    app.run(debug=True)




