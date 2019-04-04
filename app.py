import webhook
from v1.Bot import Bot

bot = Bot()

@bot.on_hears("hi")
def say_hi(room_id=None):
    return bot.send_message(room_id, "hi")

webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)