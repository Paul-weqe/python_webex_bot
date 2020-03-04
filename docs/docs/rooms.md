# Rooms 

## Get all rooms

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on here.*</span>

What we are aiming to do here is to get all the rooms that the bot is currently in. All from group rooms to individual rooms, we get all the details. Let us look at what we have to do:

```
from python_webex.v1.Bot import Bot

bot = Bot()

all_rooms_response = bot.get_all_rooms()

all_rooms = all_rooms_response.json()

print(all_rooms)

```

If everything works out fine you should see the following output:

```
{
    'items': [
        {
            'title': 'room-title', 
            'ownerId': 'consumer', 
            'id': 'room-id', 
            'teamId': 'team-id', # this will show if it is a group room
            'lastActivity': '2019-03-29T07:36:12.214Z', 
            'created': '2019-03-29T07:34:21.521Z', 
            'isLocked': False, 
            'creatorId': 'creator-id', 
            'type': 'group'
        }
    ]
}
```

## Get room details
<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

This gets the details of a specific room, we can use the output from <a href="#get-all-rooms">here</a> and get a single rooms ID. We will call the room ID <em>room_id</em>

We will use this <em>room_id</em> to get the details of that specific room, here is how:

```
from python_webex.v1.Bot import Bot

bot = Bot()

room_id = 'someroomid'

room_details_response = bot.get_room_details(room_id=room_id)

room_details = room_details_response.json()

print(room_details)

```

You should see an output similar to this: 

```
{
    'creatorId': 'creator-id', 
    'lastActivity': '2019-03-29T07:36:12.214Z', 
    'id': 'room-id', 
    'title': 'Discussion', 
    'created': '2019-03-29T07:34:21.521Z', 
    'type': 'group', 
    'ownerId': 'consumer', 
    'isLocked': False, 
    'teamId': 'team-id' # if the room is a team
}

```

Use this information wisely. 

## Create Room

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Some of the functionality for creating a room is still being worked on, bear with us. 

The following should work for creating a room:

```
from python_webex.v1.Bot import Bot

bot = Bot()

bot.create_room(title="Bot's room with best friend", team_id="team-id", room_type="something either 'direct' or 'group'")
```

## Update Room Details

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Currently, we can only edit the title of a room. To do so, run the following script:

```
from python_webex.v1.Bot import Bot

bot = Bot()

room_id = 'room-id'

bot.update_room_details(room_id=room_id, title='New Title')
```

## Delete a room

<span style="color: orange;">*Always remember that you need to have already set the value <b>auth_token</b> as your bot's Access token before you run this any of the other examples on this tutorial.*</span>

Let us wreck some havock and delete a room. 

This can be done through:

```
from python_webex.v1.Bot import Bot

bot = Bot()

room_id = 'room-id'

bot.delete_room(room_id=room_id)
```
