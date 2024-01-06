import os

API_ID = API_ID = 11454995

API_HASH = os.environ.get("API_HASH", "78718c5bffa26f1a2fcdd968ce057a58")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6735840254:AAH2iLFxvl69U0iDjS11jZ-WAZaQsOl7Bkw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6886598484))

LOG = -4033130750

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6886598484").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


