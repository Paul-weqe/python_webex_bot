
# Cards

## Create & Send Blank Card
<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Cards are meant to increase interactivity during the chat. They can be used, for example to send a form that the bot would like an end user to respond to. In this instance, we are sending a blank card to the user, which is pretty much useless. This can 


```
from python.webex.v1.Card import Card
from python.webex.v1.Bot import Bot

bot = Bot()

card = Card()

bot.send_card(card=card, room_id="room-id")
```

## Add text items on the card

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

The card we just sent above is pretty much useless. If we are to send a card, the user needs to be able to interact with the card and the bot should be able to read whatever has been input on the user side.

```
from python_webex.v1.Card import Card
from python_webex.v1.Bot import Bot

bot = Bot()

bot.create_webhook(
    name='attachment-response-2', target_url="[your-bot-url]/attachment-response", resource="attachmentActions", event="created"
)

Card = Card()
bot.send_card(card=card, room_id='room-id')
```

## Create Card Webhook

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Here, we create a webhook for the card responses. For instance, if one fills a form that has been sent on a card, the response will be sent to the specific webhook. 

```
from python_webex.v1.Card import Card
from python_webex.v1.Bot import Bot

bot = Bot()

bot.create_webhook(
    name='attachment-response-2', target_url="[your-bot-url]/attachment-response", resource="attachmentActions", event="created"
)

```

<span style="color: red;"><b>Note:</b> always make sure to setup this webhook to be whatever link you will be using and append <i>/attachment-response</i> to it. For example, if you are using 'https://abc.com', your value on target_url will be 'https://abc.com/attachment-response'</span>

## Listen for response on card

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Now, what happens when the user has filled a card form and the response has been sent to the webhook, how do we get the information about the card that has been filled from our end?

Here is how: 

```
from python_webex.v1.Card import Card
from python_webex.v1.Bot imporrt Bot
from pprint import pprint
from python_webex import webhook

bot = Bot()
card = Card()


card.add_input_text(
    input_id="first-name-input", input_placeholder="First Name"
)

card.add_input_text(
    input_id="last-name-input", input_placeholder="Last Name"
)

card.add_submit_action_btn(
    title="Submit"
)

message = bot.send_card(card=card, room_id="room-id")
message_id = message.json()['id']

@bot.attachment_response(message_id=message_id)
def respond_to_card(msg):
    pprint(msg)

webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)

```


