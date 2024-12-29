# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "23054736")
    API_HASH = environ.get("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7214222575:AAHSuRNS05nBKMB2ZSAugp8jFJXxxkA7QCU") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1352497419').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://pbot:pbot@pbot.h5n6l.mongodb.net/?retryWrites=true&w=majority&appName=pbot")
    DATABASE_NAME = environ.get("DATABASE_NAME", "pbot")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002078545756'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1001911851456") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
