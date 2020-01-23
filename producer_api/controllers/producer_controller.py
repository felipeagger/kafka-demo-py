from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from confluent_kafka import Producer
from utils.functions import corsify_response
from flask import jsonify
from os import getenv
import json


producer = Producer({'bootstrap.servers': getenv('HOST_KAFKA')+':9092'})


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def get():
    document = {
            'msg': 'Hello World, Producer API Running!'
    }

    return corsify_response(jsonify(document)), 200


def post(body):
    try:

        msg = json.dumps(body)

        producer.poll(0)
        producer.produce('topictest', msg.encode('utf-8'), callback=delivery_report)
        producer.flush()

        return corsify_response(jsonify(body)), 201            
    except Exception as e:
        return corsify_response(jsonify({'msg': 'Bad Request!', 'error': str(e)})), 400
        print(e)
