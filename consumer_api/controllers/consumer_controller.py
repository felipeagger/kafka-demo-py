import threading
import time
import json
from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from confluent_kafka import Consumer, KafkaError
from utils.functions import corsify_response
from utils.apmconfig import apm
from flask import jsonify
from os import getenv



messages = []

consumer = Consumer({
    'bootstrap.servers': getenv('HOST_KAFKA') + ':9092',
    'group.id': 'consumer_api',
    'auto.offset.reset': 'earliest',

})

consumer.subscribe(['topictest'])

#consumer.close()


def get():  
    global messages  
    return corsify_response(jsonify(messages)), 200


def read_msgs():
    global consumer
    global messages
    print('Initializing Thread Listener...')
    
    while True:
        try:
            msg = consumer.poll(1.0)

            if msg is None:
                time.sleep(1)
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            msg = 'Received message: {}'.format(msg.value().decode('utf-8'))
            messages.append({"msg": msg})
            print(msg)
        except Exception:
            apm.capture_exception()

         
# Create a Thread with the function
th = threading.Thread(target=read_msgs)
th.start()