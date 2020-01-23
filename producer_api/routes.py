from flask import request, Blueprint
from producer_api.controllers.producer_controller import *

producerRoutes = Blueprint('routes', __name__)


@producerRoutes.route('/api/producer', methods=['GET', 'POST'])
def producer():

    if request.method == 'GET':
        return get()

    if request.method == 'POST':
        return post(request.get_json())
