from spark import SparkBot

myBot = SparkBot("OWE5MzZlMWMtMWVjNS00ZDY4LTliYTctYzM3NTYxMWUwMzZmMTZkMGNjZmYtMTg1")
active_bot = myBot


@myBot.onHears("Hello")
def respond_hello():
	myBot.sendMessage("Y2lzY29zcGFyazovL3VzL1JPT00vMTY0ODJkZmUtYmEyZS0zYjE1LWFkNDUtMGRjOWQ2N2Q0NGMy", "Killed this")

