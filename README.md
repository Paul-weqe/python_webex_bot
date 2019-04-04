[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/Paul-weqe/python_webex_bot)
[![PyPI version](https://badge.fury.io/py/python-webex-bot.svg)](https://badge.fury.io/py/python-webex-bot)

# python_webex_bot

A python3 library meant to help you create a cisco webex teams bot and take advantage of some of the features available to these bots. 
Most of the python libraries setup for webex have been lacking in terms of connecting you to a webhook and this aims at solving that

## Installation and setup

The following are items this documentation assumes you already have installed
- virtualenv
- python3
- <a href="https://ngrok.com/download">ngrok</a>

### Step 1: setup the virtual environment

to initialize the virtual environment, run the following command in your Command Line or Command Prompt
```
virtualenv venv
```

then we activate it:

<i>Windows</i>
```
venv\Scripts\activate
```

<i>Linux</i>
```
source venv/bin/activate
```

and there, you have your virtual environment setup and ready for action

### Step 2: install python_webex_bot

while still in your activated virtual environment, run the following command to install python_webex_bot via pip:

```
pip install python_webex_bot
```

then download <a href="https://ngrok.com/download">ngrok</a> which will be used in the concurrent steps

## Quickstart

Lets get a simple bot up, running and responsive on our local machine. 

### Step 1: Create the bot on Cisco Webex

If you haven't already, <a href="https://teams.webex.com/signin">create your Webex account.</a> 
Then head on to <a href="https://developer.webex.com/my-apps/new/bot">create your bot</a>

You should be provided with an <u>access token </u> for the bot.

Take this access token and place it in your environment variable as auth_token.

this can be done via your Command prompt or Command Line as:
```
set auth_token=my_auth_token
```

replace my_auth_token with your bots access token

<b>This is a crutial part of running your bot as the python_webex_bot library uses this to identify your bot</b>

If you still have some questions on environment variables, why we need them and how to use them, <a href="https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa">this</a> may be a good start

### Step 2: setup ngrok

in a different terminal from the one used in steps 1 and 2, navigate to the folder where you have the ngrok placed. 

Then run the following command:
```
ngrok http 5000
```

This should produce an output similar to the one shown below:
```
Session Status                online
Session Expires               7 hours, 59 minutes
Update                        update available (version 2.3.25, Ctrl-U to update)
Version                       2.3.18
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://87a942a1.ngrok.io -> http://localhost:5000
Forwarding                    https://87a942a1.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

<i>Now you are ready for the quest</i>

### Step 3: create the python file and run it 

Create a python file where you intend to run the bot. In my case, I will name my file `run.py`

copy and paste the following code:

```
from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot()         # the program will automatically know the bot being referred to y the auth_token

# create a webhook to expose it to the internet
# rememer that url we got from step 2, this is where we use it. In my case it was http://87a942a1.ngrok.io. 
# We will be creating a webhook that will be listening when messages are sent
bot.create_webhook(
    name="quickstart_webhook", target_url="http://87a942a1.ngrok.io", resource="messages", event="created"
)

# we create a function that responds when someone says hi
# the room_id will automatically be filled with the webhook. Do not forget it
@bot.on_hears("hi)
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="Hi, how are you doing?")

# We create a default response in case anyone types anything else that we have not set a response for
# this is done using * [ don't ask me what happend when someone sends '*' as the message, that's on my TODO]
@bot.on_hears("*")
def default_response(room_id=None):
    return bot.send_message(room_id=room_id, text="Sorry, could not understand that")


# make the webhook know the bot to be listening for, and we are done
webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)         # don't keep debug=True in production
```

Now, when we text our bot "hi", it will respond with "Hi, how are you doing?"

And when we text anything else, like "When can we meet up?" it will respond with "Sorry, I could not understand that"


<b><i>MORE DOCUMENTATION TO BE SETUP SHORTLY</i></b>
