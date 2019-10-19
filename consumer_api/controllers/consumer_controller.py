#Dependencies
from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env_')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from kafka import KafkaConsumer
from datetime import datetime
from utils.functions import corsify_response
from flask import jsonify
from os import getenv
import threading
import time
import json
import requests

# Create an instance of the Kafka producer
consumer = KafkaConsumer('topictest', 
bootstrap_servers= getenv('HOST_KAFKA')+':9092',
auto_offset_reset='earliest',
enable_auto_commit=True,
group_id='consumer_api',
value_deserializer=lambda m: json.loads(m.decode('ascii')))


#GET
def get():    
    document = {
            'msg': 'Hello World, Consumer API Running!'
    }
    return corsify_response(jsonify(document)), 200


def ReadMsgs():
    global consumer
    print('Initializing Thread Listener...')
    for msg in consumer:
        print('offset {} - {}'.format(msg.offset, msg.value))
        time.sleep(1)


# Create a Thread with a function without any arguments
th = threading.Thread(target=ReadMsgs)

# Start the thread
th.start()