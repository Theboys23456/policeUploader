#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24037760"))
API_HASH = environ.get("API_HASH", "dccc3070f1c12ab155011f14c3d6ae6a")
BOT_TOKEN = environ.get("BOT_TOKEN", "7595438234:AAHkW3sI5O-2_3BOLgEAtrr1jpyCBloPwDI")

OWNER = int(environ.get("OWNER", "8167879352"))
CREDIT = environ.get("CREDIT", "ǟʟʟ ƈʟǟֆֆɛֆ ʍօʀɛռǟ一")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7290128282, 8167879352').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7290128282, 8167879352').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set





