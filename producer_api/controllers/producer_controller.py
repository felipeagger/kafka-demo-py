from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from kafka import KafkaProducer
from producer_api.utils.functions import corsify_response
from flask import jsonify
from os import getenv
import json


producer = KafkaProducer(bootstrap_servers=getenv('HOST_KAFKA')+':9092',
    value_serializer=lambda m: json.dumps(m).encode('ascii'))

# string data
# value_serializer=lambda v: str(v).encode('utf-8')) 


def get():
    document = {
            'msg': 'Hello World, Producer API Running!'
    }

    return corsify_response(jsonify(document)), 200


def post(body):
    try:

        producer.send('topictest', body)

        return corsify_response(jsonify(body)), 201            
    except Exception as e:
        return corsify_response(jsonify({'msg':'Bad Request!', 'error': str(e)})), 400
        print(e)
