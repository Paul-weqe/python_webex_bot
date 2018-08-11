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

Once inside the weqe_sparkbot, you will have the following directory structure:
```
app.py
requirements.txt
spark.py
test.py
```

## Explanation of the files
##### 1. app.py

This is the main file where the webhook will be created and actively listening. This has two functions ( meant to increase in future ) that are actively listening, primarily for messages that are directed to it (the `@app.route("/message")` in the file)

This folder will therefore detect immediately when an action takes place. For instance, a message is sent to the bot or the bot is mentioned in a room somewhere.

##### 2. spark.py

This file holds the main API class, SparkBot. Using this class, a user can create an object based on the user's specific bot that they want to create in the test.py file ( to be described shortly ). This file also adds specific functionality of the bot like sending a message, attaching a file and other items.

##### 3. test.py

This is where the programmer will write the actual code that will be running the bot. For example, the following lines may be written in the file to create an instance and to take an action

```
from spark import SparkBot

myBot = SparkBot("my_authentication_token") # in place of my_authentication_key enter your bot's authentication key
active_bot = myBot   # this lets the app.py file that contains the webhooks to know which object it will be communicating                           # with when receiving the messages

@active_bot.onHears("Hi")
def hear_function():
    print("He said hi...")
```

*More documentation to be uploaded soon enough*
