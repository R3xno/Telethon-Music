import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20558450"))
    API_HASH = os.environ.get("API_HASH", "206db5264a2608e01d3500b90f00e13e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7582864839:AAHunJDb_snPJ2u79nVhtjJIydzThwRofG8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIwBu5_1prmYxne3RjoT23tJ5jibJ4fliZsRCm_jSc7GJQrlbRgNetlb2KCShZJpXBgtjMThivYO0Eo2TN_H5ZDsNPU3WGtjpNbOfp4eToP76LBERlgOlF-mke7caCVjQpJmTrrp7V4A01J4Dc_f66zA2yf3nS2tONmItZG-EICWQSc-Bh4E9rNmSvW1pxMyDJstnsXNDfM_Ru1yf0HPLsJJEKyS3-2aOtHpI78dofX0MI-ZVGf3zuMWZtXU7ErMgv9kJJ9dlDTsaOTzlKFuPxPY8swacsgRqW-L3L3n4n4hK61pRBoX6mPn9bMT-7DJF7i1z3CvkuNy0jHOfnklVfUvD9Q=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "CherryXMusic_Robot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2099083519")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
