from telegram import Bot
import os 
import time
from pprint import pprint

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info
# pprint(bot.getUpdates())
def main():
    last_update = bot.getUpdates()
    last_update_id = last_update['update_id']

    while True:
        curr_update = bot.getUpdates()
        curr_update_id = curr_update['update_id']
        # 
        if curr_update_id != last_update_id:
            chat_id = curr_update['message']['from']['id'] 
            keys = list(curr_update['message'].keys())
            # 
            if 'photo' in keys:
                file_id = curr_update['message']['photo'][0]['file_id']
                bot.sendPhoto(chat_id, file_id)
                last_update_id = curr_update_id
            elif 'sticker' in keys:
                file_id = curr_update['message']['sticker']['file_id']
                bot.sendSticker(chat_id, file_id)
                last_update_id = curr_update_id
            elif 'text' in keys:
                text = curr_update['message']['text']
                bot.sendMessage(chat_id, text)
                last_update_id = curr_update_id
            elif 'document' in keys:
                file_id = curr_update['message']['document']['file_id']
                bot.sendDocument(chat_id,file_id)
                last_update_id = curr_update_id
            elif 'video' in keys:
                file_id = curr_update['message']['video']['file_id']
                bot.sendVideo(chat_id,file_id)
                last_update_id = curr_update_id
            elif 'location' in keys:
                latitude = curr_update['message']['location']['latitude']
                longitude = curr_update['message']['location']['longitude']
                bot.sendLocation(chat_id,latitude,longitude)
                last_update_id = curr_update_id
            elif 'contact' in keys:
                first_name = curr_update['message']['contact']['first_name']
                phone_number = curr_update['message']['contact']['phone_number']
                bot.sendContact(chat_id,first_name,phone_number)
                last_update_id = curr_update_id
        
        time.sleep(1)

main()