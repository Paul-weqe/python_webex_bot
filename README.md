# weqe_chatbot

weqe_chatbot is a python library that is meant to provide an easy way for developers to create constant and active webhook. The project will mainly involve listening through a flask webhook and having the bot's actions performed according to sprcific ways that are specified by the programmer. 

## getting started

### prerequisites

The following are the mininimal requirements that are required by the time you have downloaded the repository to get it up and running:
	- python3
	- virtualenv

You download the required files by entering the following line in your terminal

```
git clone https://github.com/Paul-weqe/weqe_sparkbot.git
```

After this, go into the folder that has been cloned

```
cd weqe_sparkbot
```

Then create a virtual environment to work with and activate it:
```
virtualenv -p python3 venv
source venv/bin/activate
```

### installation

Install all the requirements to be able to run the application successfully
`pip3 install -r requirements.txt`

### running the app

start the flask app, which will act as the webhook. Type the following command in the terminal

`python3 app.py`

You may then start a webhook that is exposed to the internet via ngrok or any other tunnelling software. Download ngrok for ubuntu by clicking [ngrok download](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip). Once downloaded, extract the file and navigate to the folder where you extracted the file at, then run the following command:

`./ngrok http 5000`

This should be enough to expose the app to the internet. Follow the following link to find more information of how to create a spark webhook [Creating cisco spark webhook](https://developer.webex.com/endpoint-webhooks-post.html).

*If you close the ngrok service and start it again, make sure to create the webhook again via the cisco spark tutorial*

## writing a basic bot

You have to write your code in the test.py file, which is where the webhook will be listening for any messages that are directed to the bot. The following is a sample of a program that will say "Hi too" to anyone who says "Hi"

```
from spark import SparkBot

myBot = SparkBot("your_auth_key")
active_bot = myBot 		# this line is crutial for the webhook to know which bot is being specified to listen to

@myBot.onHears("Hi")
def respond_to_hi():
    room_id = myBot.message_data["roomId"]
    myBot.sendMessage(room_id, "Hi too")
```

## attaching file while responding to a message

One may also need to attach a file while sending a response to a specific event. The following is how the function to do this will be written:

```
@myBot.onHears("send me an image")
def send_image():
    room_id = myBot.message_data["roomId"]
    myBot.sendAttachment(room_id, "https://pbs.twimg.com/profile_images/831938838935203840/eGVNy9b7_400x400.jpg")
```

## respond to mention from a space

The following is if one wants to respond to when someone mentions the bot in a space or a room:

```
@myBot.onHears("send me something", mention=True)
def respond_to_mention():
    room_id = myBot.message_data["roomId"]
    myBot.sendAttachment(room_id, "https://pbs.twimg.com/profile_images/831938838935203840/eGVNy9b7_400x400.jpg")
```

## Explanation of the files
##### 1. app.py

This is the main file where the webhook will be created and actively listening. This has two functions ( meant to increase in future ) that are actively listening, primarily for messages that are directed to it (the `@app.route("/message")` in the file)

This folder will therefore detect immediately when an action takes place. For instance, a message is sent to the bot or the bot is mentioned in a room somewhere.

##### 2. spark.py

This file holds the main API class, SparkBot. Using this class, a user can create an object based on the user's specific bot that they want to create in the test.py file ( to be described shortly ). This file also adds specific functionality of the bot like sending a message, attaching a file and other items.

##### 3. test.py

This is where the programmer will write the actual code that will be running the bot. For example, the following lines may be written in the file to create an instance and to take an action

*More features will be added and the documentation will be updated to fit the growth. Have a blast, and feel free to contribure. :)*
