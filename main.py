from telegram import Bot
import os 

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info


# Send a message to the bot
chat_id = ''
msg = bot.sendMessage(chat_id,"Hello World!!!")
print(msg.text)