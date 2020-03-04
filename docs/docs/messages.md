
# Messages

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

