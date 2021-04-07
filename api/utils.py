from api.data_models import *
from api.database import new_entry
from flask import jsonify
from api.config import ADMIN_TOKEN

def get_entry(EntryType, Selector):
    