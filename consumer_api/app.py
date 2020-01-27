from os import getenv
from dotenv import load_dotenv
from os.path import dirname, isfile, join

# setting enviroment file
_ENV_FILE = join(dirname(__file__), '.env')
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from config import config
from routes import consumerRoutes
from utils.apmconfig import apm


def create_app(config_name):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config[config_name])

    app.config["DEBUG"] = True

    # app.config['ELASTIC_APM'] = {
    #     'SERVICE_NAME': 'kafka-consumer-api',
    #     'SERVICE_VERSION': '1.0.0',
    #     'SERVER_URL': 'http://' + getenv('HOST_APM') + ':8200',
    #     'SECRET_TOKEN': '',
    #     'CAPTURE_BODY': 'all',
    #     'DEBUG': True,
    #     'SERVER_TIMEOUT': 2
    # }

    # apm.init_app(app)
    CORS(app)
    return app


app = create_app(getenv('FLASK_ENV') or 'default') 

app.register_blueprint(consumerRoutes)

@app.route('/index')  
def send_index():  
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/swagger.json')  
def send_file():  
    return send_from_directory(app.static_folder, 'swagger.json')


SWAGGER_URL = '/api-docs'
API_URL = '/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Consumer-API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )