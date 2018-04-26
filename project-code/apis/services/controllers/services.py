import yaml
from flask import jsonify

import config

def search():
    return jsonify(config.apis)
