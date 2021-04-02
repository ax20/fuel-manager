from flask import Flask, request

api = Flask(__name__)
api.config['DEBUG'] = True
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from entry import *

@api.route('/v1/<EntryType>/<Selector>/', methods=['GET'])
def get_all(EntryType, Selector):
    reply = get_all_entries(EntryType, Selector)

    return jsonify(reply)

@api.route('/v1/<EntryType>/<Selector>/', methods=['POST'])
def push_item(EntryType, Selector):
    answer = push_entry(EntryType, Selector, request.get_json())
    return answer