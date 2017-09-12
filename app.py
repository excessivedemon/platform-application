import awsgi
from flask import Flask
from flask_restful import Resource, Api
from time import time
import requests

app = Flask(__name__)
api = Api(app)

def get_from_file(filename):
  with open(filename) as f:
    lines = f.read().splitlines()
    if lines:
      return lines[0]
    else:
      return 'n/a'

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
    start = time()
    response = requests.get(url)
    response_time = round(time() - start, 2)
    return dict(status_code=response.status_code, response_time=response_time), 200

api.add_resource(HelloWorld, '/', '/root')
api.add_resource(MetaData, '/metadata')
api.add_resource(Health, '/health')

def lambda_handler(event, context):
  return awsgi.response(app, event, context)
