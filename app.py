from flask import Flask, request

api = Flask(__name__)
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from api.utils import *

# Example: /v1/Fuel/Matryx2007/all, /v1/Fuel/Yaris2011/all
@api.route('/v1/<EntryType>/<Selector>/all', methods=['GET'])
def get_item(EntryType, Selector):
    reply = fetch_item(EntryType, Selector)