import requests
from .message import Message


class Bot:
    def __init__(self,token:str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def getMe(self):
        """
        A simple method for testing your bot's auth token. Requires no parameters. 
        Returns basic information about the bot in form of a User object.
        """
        url = f'{self.base_url}getMe'
        # Requesting the url
        response = requests.get(url)
        # Converting the response to json
        response = response.json()
        # Returning the response
        return response

    def sendMessage(self,chat_id:int,text:str):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            text: Text of the message to be sent
        returns:
            A message object
        """
        # Defining the url to send the message
        url = f'{self.base_url}sendMessage'
        # Defining the data to send
        data = {
            'chat_id':chat_id,
            'text':text
        }
        # Sending the message
        response = requests.get(url,params=data)
        # Converting the response to json
        
        return response.status_code

    def getUpdates(self,offset:int=None):
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.
        args:
            offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
        returns:
            An array of update objects
        """
        # Defining the url to update
        url = f'{self.base_url}getUpdates'

        response = requests.get(url)
        return response.json()['result'][-1]

    def sendPhoto(self,chat_id:int,photo:str):
        """
        Use this method to send photos. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data.
        returns:
            A message object
        """
        url = self.base_url + 'sendPhoto'
        payload = {
            'chat_id': chat_id,
            'photo': photo
        }
        response = requests.get(url, json=payload)
        return response.status_code

    def sendSticker(self,chat_id:int,sticker:str):
        """
        Use this method to send .webp stickers. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            sticker: Sticker to send. Pass a file_id as String to send a sticker that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data.
        returns:
            A message object
        """
        url = self.base_url + 'sendSticker'
        payload = {
            'chat_id': chat_id,
            'sticker': sticker
        }
        response = requests.get(url, json=payload)
        return response.status_code

    def sendDocument(self,chat_id:int,document:str):
        """
        Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        returns:
            A message object
        """
        url = self.base_url + 'sendDocument'
        payload = {
            'chat_id':chat_id,
            'document':document
        }
        response = requests.get(url,json=payload)
        return response.status_code

    def sendVideo(self,chat_id:int,video:str):
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video file using multipart/form-data.
        returns:
            A message object
        """
        url = self.base_url + 'sendVideo'
        payload = {
            'chat_id':chat_id,
            'video':video
        }
        response = requests.get(url,json=payload)
        return response.status_code

    def sendLocation(self,chat_id:int,latitude:float,longitude:float):
        """
        Use this method to send point on the map. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            latitude: Latitude of location
            longitude: Longitude of location
        returns:
            A message object
        """
        url = self.base_url + 'sendLocation'
        payload = {
            'chat_id':chat_id,
            'latitude':latitude,
            'longitude':longitude
        }
        response = requests.get(url,json=payload)
        return response.status_code

    def sendContact(self,chat_id:int,phone_number:str,first_name:str):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            phone_number: Contact's phone number
            first_name: Contact's first name
        returns:
            A message object
        """
        url = self.base_url + 'sendContact'
        payload = {
            'chat_id':chat_id,
            'first_name':first_name,
            'phone_number':phone_number
        }
        response = requests.get(url,json=payload)
        return response.status_code

    
      

