import awsgi
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from time import time
import requests

app = Flask(__name__)
api = Api(app)
CORS(app)

def get_from_file(filename):
    try:
        with open(filename) as f:
            lines = f.read().splitlines()
            return lines[0]
    except Exception:
        return None

class HelloWorld(Resource):
    def get(self):
        return dict(message='Hello World'), 200

class MetaData(Resource):
    def get(self):
        return dict(
            version=get_from_file('version'),
            lastcommitsha=get_from_file('source_hash')), 200

class Health(Resource):
    def get(self):
        url = get_from_file('health')
        print url
        status_code = None
        response_time = None
        start = time()
        if url:
            response = requests.get(url)
            status_code = response.status_code
            response_time = round(time() - start, 2)
        return dict(status_code=status_code, response_time=response_time), 200

api.add_resource(HelloWorld, '/', '/root')
api.add_resource(MetaData, '/metadata')
api.add_resource(Health, '/health')

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)
