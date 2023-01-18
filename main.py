from telegram import Bot
import os 

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info

print(bot.getMe())