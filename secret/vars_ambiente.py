import os
import json

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PRIVATE_KEY_1 = os.getenv("private_key_1")
PRIVATE_KEY_2 = os.getenv("private_key_2")
create_secret = str(PRIVATE_KEY_1 + PRIVATE_KEY_2)
MY_SECRETS = json.loads(create_secret)
DIRECTORY = os.getenv("Directory")

