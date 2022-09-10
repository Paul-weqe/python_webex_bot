
# Messages

## Create Message

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Want to send a message from your bot to a specific room? No worries, here is how:

```python
from python_webex.v1.Bot import Bot

bot = Bot()

bot.send_message(to_person_email='person-email@gmail.com', text='This is some text')
# or
bot.send_message(room_id='someroomid', text='This is the text')

# you can use either `room_id` will be given priority over `to_person_email` when both are used at the same time. 
```


## Attach files with message
<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

To attach a files when sending a message, do this:
```
from python_webex.v1.Bot import Bot

bot = Bot()

bot.send_message(room_id='room-id', text='I am sending a file', files=['https://image.shutterstock.com/image-photo/white-transparent-leaf-on-mirror-260nw-1029171697.jpg'])
```

<span style="color:red;"><b>Note</b> the <i>files</i> parameter may be a list, but only one field is allowed. Why Exactly? No Idea, ask Webex. And also you can only keep URI's on the files field and not a path to a file in a local directory. <span>

## Get messages

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

This lists all the messages that have been received by the bot on a specific room.

This is how we can get these details:

```
from python_webex.v1.Bot import Bot
from pprint import pprint

bot = Bot()

pprint(bot.get_messages(room_id="room-id").json())
```

## Get Direct Messages

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Gets a list of all messages sent in 1:1 rooms. This is basically a list of all the bot's DMs with a particular individual, done by providing the person's ID.

This is how this is done:

```
from python_webex.v1.Bot import Bot
from pprint import pprint

bot = Bot()

pprint(bot.get_direct_messages(person_id="person-id").json())
```


## Get Message Details

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Gives you details about a specific message with ID <b><i>message-id</i></b>

```
from python_webex.v1.Bot import Bot
from pprint import pprint

bot = Bot()

pprin(bot.get_message_details(message_id="message-id").json())
```

## Delete Message 

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Deletes a specific message with ID <b><i>message-id</i></b>

```
from python_webex.v1.Bot import Bot
from pprint import pprint

bot = Bot()

bot.delete_message(message_id='message-id')
```

## Setup Webhook for incoming messages
<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

If your bot need to be constantly listening for incoming messages, you need to set up a webhook. To set up a webhook, you need an address that is available via the public internet. You can use <a href="https://ngrok.com/">ngrok</a> for this. 

If you have ngrok downloaded, type `./ngrok http 5000` if you are on <i>Linux</i>. Otherwise, type `ngrok.exe http 5000` if you are on <i>Windows</i>. This will give you an output as such:

```
Session Expires               7 hours, 6 minutes                                
Version                       2.3.35                                            
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    http://cff51342.ngrok.io -> http://localhost:5000 
Forwarding                    https://cff51342.ngrok.io -> http://localhost:5000
```

Now, you can open up your text editor and type in the following:
```
from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot()
bot.create_webhook(
    name='some-normal-webhook', target_url='https://cff51342.ngrok.io', resource='messages', event='created'
)

webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)
```

You willl now be constantly listening for any incoming message via the message that has been sent to the bot. 

## Set default action for incoming message

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples 
on this tutorial.*</span>

When you receive a message, it normally comes with text. The following is how to set a default response whatever text is sent to the bot:

```
from python_webex.v1.Bot import Bot

bot = Bot()

@bot.on_hears("*")
def default_on_hears_function(room_id=None):
    bot.send_message(room_id=room_id, text="This is the default response for the message that has been sent")
```

## Set default listener for incoming files

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples 
on this tutorial.*</span>

You want your bot to receive files? So do many other people. 

We need to have a way to handle how these files are received and handled. So here is how we set the default function for handling incoming files:

```
from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot()

@bot.set_default_file_response()
def default_file_response(files, room_id=None):
    bot.send_message(room_id=room_id, text='this is the default response for an attached file')

webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)

```

If you need to attach anything in the response, refer to the previous tutorial about attaching files with messages

## Set listener for specific text attached with file

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples 
on this tutorial.*</span>

What do you do when someone send you a file attached with a specific set of text, and you do know what you need your bot to do at this point:

```
from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot()

@bot.set_file_action("This is me")
def custom_response(room_id=None, files=None):
    print(files)
    bot.send_message(room_id=room_id, text="You look amazing")

webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)

```

In `def custom_response(room_id=None, files=None):`, files represent a list of the files being sent to the bot. 