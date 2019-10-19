from flask import jsonify, request, Blueprint
from utils.functions import corsify_response
from controllers.consumer_controller import *

consumerRoutes = Blueprint('routes', __name__)

### ---- Routes ---- ###

###  /api/consumer  ###
@consumerRoutes.route('/api/consumer', methods=['GET', 'POST'])
def consumer():

    ### GET ###
    if (request.method == 'GET'):
        return get()


    ### POST ###
    if (request.method == 'POST'):
        return post(request.get_json())