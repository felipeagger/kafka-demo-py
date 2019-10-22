import json
import pytest
from random import randint
from os.path import dirname, isfile, join, abspath
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

_ENV_FILE = join(dirname(__file__), '.env_')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from app import app #create_app

@pytest.fixture(scope='session')
def client():    
    #flask_app = create_app('testing') 
    client = app.test_client()
    return client

def test_producer_Post_response_201(client):    
    body = {
        'test_id': 1,
        'test_name': 'Description Test'
    }

    response = client.post('/api/producer', json=body)
    #orderid = response.json['_id']
    assert response.status_code == 201

def test_producer_Get_response_200(client): 
    response = client.get('/api/producer')
    
    #status_code = 200
    assert response.status_code == 200    
    assert len(response.json) > 0