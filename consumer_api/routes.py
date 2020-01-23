import threading
from flask import jsonify, request, Blueprint
from utils.functions import corsify_response
from controllers.consumer_controller import *

consumerRoutes = Blueprint('routes', __name__)


@consumerRoutes.route('/api/consumer', methods=['GET', 'POST'])
def consumer():

    if request.method == 'GET':
        return get()

    if request.method == 'POST':
        th = threading.Thread(target=read_msgs)
        th.start()
        return corsify_response(jsonify({'msg': 'Ok'})), 200
