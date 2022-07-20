from urllib import response
from flask import Flask
from flask_restful import Api, Resource
import requests
import json
import os


port = int(os.environ.get('PORT'))

def read_json(_file: str):
    '''
    Read a JSON file and return the data.

    _file -- the JSON file to read from.

    return -- a list of records in the data.
    '''
    with open(_file, 'r') as j:
        _records: list = json.loads(j.read())
    return _records


def past_records(data, n):
    data = data[-n:]
    return data


# file: str = "https:/ccy05327.github.io/Sleep-Data-Visualization/output/SDV.json"
file = "https://raw.githubusercontent.com/ccy05327/Sleep-Data-Visualization/main/output/SDV.json"
response = (requests.get(file)).json()['sleep_record']

app = Flask(__name__)
api = Api(app)


class record(Resource):
    def get(self):
        return {"sleep_record": response}


class past_record(Resource):
    def get(self, length):
        return {"sleep_record": past_records(response, length)}


api.add_resource(record, "/")
api.add_resource(past_record, "/<int:length>")

if __name__ == '__main__':
    app.run(debug=True, port=port)
