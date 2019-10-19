from flask import jsonify, request, Blueprint
from utils.functions import corsify_response
from controllers.producer_controller import *

producerRoutes = Blueprint('routes', __name__)

### ---- Routes ---- ###

###  /api/producer  ###
@producerRoutes.route('/api/producer', methods=['GET', 'POST'])
def producer():

    ### GET ###
    if (request.method == 'GET'):
        return get()


    ### POST ###
    if (request.method == 'POST'):
        return post(request.get_json())