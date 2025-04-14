"""
from os import getenv


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "7503125213:AAFsRIHoAwlQ3R-")
OWNER_ID = int(getenv("OWNER_ID", "7507228967"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://:<>@cluster0.aigsy.mongodb.net/?=true&wmajority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

