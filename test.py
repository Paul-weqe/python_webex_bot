from spark import SparkBot

myBot = SparkBot("OWE5MzZlMWMtMWVjNS00ZDY4LTliYTctYzM3NTYxMWUwMzZmMTZkMGNjZmYtMTg1")
active_bot = myBot


@myBot.onHears("Hello")
def respond_hello():               
	room_id = myBot.message_data["roomId"]
	# room_id = myBot.message_data["roomId"]
	print("Room id {}".format(room_id))
	myBot.sendMessage(room_id, "Sure?")

@myBot.onHears("Send me something")
def send_attachment():
	room_id = myBot.message_data["roomId"]
	myBot.send_attachment(room_id, ["http://e1.365dm.com/18/08/16-9/20/skysports-maurizio-sarri-chelsea_4385919.jpg?20180810133729"])
	return None