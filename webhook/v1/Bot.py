import sys

class Bot:

    def onHear(self, text=None):
        if text == None:
            sys.exit("'text' cannot be empty")
        
        print(text)