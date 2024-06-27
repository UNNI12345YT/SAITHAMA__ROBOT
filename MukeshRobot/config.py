
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 27408015 # integer value, dont use ""
    API_HASH = "2f07e7c921c8d2b982df12d65a46ca46"
    TOKEN = "7474172596:AAFKvnrFM5a25xCOzVgejImLRTujDEsQ3ec"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6171681404 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "MRXSUPPORT"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/9e19a80a14adb745c80c8.gif"
    EVENT_LOGS = (-1002090641762)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://Achu:Achu@cluster0.shz28r2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "WYHK8S2IRO0M50BX"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    
    # Get your API key from https://timezonedb.com/api


    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [6171681404]  # User id of sudo users
    DEV_USERS = [6171681404]  # User id of dev users
    DEMONS = [5758713974]  # User id of support users
    TIGERS = [5758713974]  # User id of tiger users
    WOLVES = [6171681404]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
