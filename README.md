weqe_sparkbot is a python library meant to easen the creation of bots within the Cisco Webex for Teams using python(popularly Cisco spark). 

There have been previous solutions that have been implemented but the main issue being the creation of constant webhooks. This prject plans to use Flask to maintain and listen on these webhooks and thus one can receive immediate update when e.g a message is sent to the bot. This solution is also meant to be minimalistic and will only go more that five files if conditioins force this to happen. We hope to give you a good python3 webex solution by the end of this project. 

*Development is currently underway, join in if interested. Documentation will be out soon enough* 

You can get the library by entering the following line in your terminal

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

Install all the requirements to be able to run the application successfully
`pip3 install -r requirements.txt`

start the flask app, which will act as the webhook. Type the following command in the terminal

`python3 app.py`

You may then start a webhook that is exposed to the internet via ngrok or any other tunnelling software. Download ngrok for ubuntu by clicking [ngrok download](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip). Once downloaded, extract the file and navigate to the folder where you extracted the file at, then run the following command:

`./ngrok http 5000`

This should be enough to expose the app to the internet. Follow the following link to find more information of how to create a spark webhook [Creating cisco spark webhook](https://developer.webex.com/endpoint-webhooks-post.html).

*If you close the ngrok service and start it again, make sure to create the webhook again via the cisco spark tutorial*


## Explanation of the files
##### 1. app.py

This is the main file where the webhook will be created and actively listening. This has two functions ( meant to increase in future ) that are actively listening, primarily for messages that are directed to it (the `@app.route("/message")` in the file)

This folder will therefore detect immediately when an action takes place. For instance, a message is sent to the bot or the bot is mentioned in a room somewhere.

##### 2. spark.py

This file holds the main API class, SparkBot. Using this class, a user can create an object based on the user's specific bot that they want to create in the test.py file ( to be described shortly ). This file also adds specific functionality of the bot like sending a message, attaching a file and other items.

##### 3. test.py

This is where the programmer will write the actual code that will be running the bot. For example, the following lines may be written in the file to create an instance and to take an action

```
@myBot.onHears('How are you?')
def respond_to_hi():
	room_id = myBot.message_data["roomId"] # the message_data contains information about the most recent message.
										   # You can just type print(message_data) to see what other information it holds
    myBot.sendMessage(room_id, "Im fine")


# to send an attachment when a user requires one, write the following
@myBot.onHears("Send me a file")
def send_file(): 
	room_id = myBot.message_data["roomId"]
	myBot.send_attachment(room_id, ["link_to_attached file"]) # replace link_to_attached_file 

	# take note that the link put cannot be a path to a file in your directory. It must be a file from a server online or something like that
	# for example 'link_to_attached_file' may be 'https://sample_site.com/image.jpg'

```

*More documentation and more improvements to be uploaded soon enough*
*Reach out to any of the contributor(s) for any help or constructive feedback that may help in improvement of the library :)*
