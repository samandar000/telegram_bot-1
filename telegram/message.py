class Message:
    def __init__(self,message:dict):
        self.message_id = message['message_id']
        self.from_user = message['from']
        self.text = message['text']