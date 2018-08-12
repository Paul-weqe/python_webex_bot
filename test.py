from spark import SparkBot

"""

This is where you will be writing the whole of your code
This is how you write the code for a simple bot that responds 'Im good' when the user sends 'How are you?'

-------

from spark import SparkBot

myBot = SparkBot("bot_access_token")    # in place of bot_access_token, enter your own bot's access token
active_bot = myBot 						# don't ever forget this line. It tells the app.py webhook listener the SparkBot object it will be sending the data received to

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

-------

"""

from spark import SparkBot

myBot = SparkBot("OWE5MzZlMWMtMWVjNS00ZDY4LTliYTctYzM3NTYxMWUwMzZmMTZkMGNjZmYtMTg1")
active_bot = myBot

@myBot.onHears("Hi")
def respond_to_hi():
	room_id = myBot.message_data["roomId"]
	myBot.sendMessage(room_id, "hi there too :)")

@myBot.onHears("Cool", mention=True)
def respond_to_cool_mention():
	room_id = myBot.message_data["roomId"]
	myBot.sendMessage( room_id, "coooool")

@myBot.onHears("Sarri", mention=True)
def respond_to_sarri_mention():
	room_id = myBot.message_data["roomId"]
	myBot.send_attachment(room_id, "https://cdn.images.express.co.uk/img/dynamic/67/590x/Chelsea-team-news-1002186.jpg?r=1534028634745")
	myBot.sendMessage(room_id, "There you go")