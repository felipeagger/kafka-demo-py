import faust
import base64
import random
import requests
from datetime import datetime
# from os import getenv
# from dotenv import load_dotenv
# from os.path import dirname, isfile, join

# # setting enviroment file
# _ENV_FILE = join(dirname(__file__), '.env')
# if isfile(_ENV_FILE):
#     load_dotenv(dotenv_path=_ENV_FILE)

# from os import getenv
# from models.message import OriginalMessage, TransformedMessage

SOURCE_TOPIC="input_users"
TARGET_TOPIC="output_users"

app = faust.App("messages-stream", 
    broker="kafka://"+'broker:29092', # getenv('HOST_KAFKA')
    topic_partitions=1,
    store="memory://")

class Username(faust.Record):
    username: str


class UserData(faust.Record):
    user_id: int
    login: str
    name: str
    avatar_url: str
    bio: str 
    location: str
    blog: str
    created_at: float
    source_topic: str
    target_topic: str


topic = app.topic(SOURCE_TOPIC, value_type=Username)
out_topic = app.topic(TARGET_TOPIC, partitions=1)

table = app.Table(
    "output_users",
    default=UserData,
    partitions=1,
    changelog_topic=out_topic,
)

print('Initializing Thread Processor...')


@app.agent(topic)
async def transformedmessage(userevents): # .group_by(Station.station_id)
    async for transfuser in userevents:
        try:

            if transfuser.username:
                request = requests.get(f"https://api.github.com/users/{transfuser.username}")

                if request.status_code == 200:
                    user = request.json()

                    _user = UserData(
                        user_id=user['id'], 
                        login=user['login'],
                        name=user['name'],
                        avatar_url=user['avatar_url'],
                        bio=user['bio'],
                        location=user['location'],
                        blog=user['blog'],
                        created_at=user['created_at'],
                        source_topic=SOURCE_TOPIC,
                        target_topic=TARGET_TOPIC)
                    
                    table[f"User_{_user.login}"] = _user

                    print(f"User {_user.login} processed!")

            # random.randint(1, 999999)
            # base64.b64encode(transfmessage.msg.encode("utf-8"))
            # datetime.now().isoformat()
        
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app.main()
