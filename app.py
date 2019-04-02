import webhook
from v1.Bot import Bot

bot = Bot()

@bot.on_hears("hi")
def hears_hi():
    return bot.send_message("Y2lzY29zcGFyazovL3VzL1JPT00vNGZjNzliMWItODg3Mi0zYThlLTk3MGItZDNlYmQ4YmI2ZTc3", "Cool..")

webhook.bot = bot


if __name__ == "__main__":
    webhook.app.run(debug=True)
