import yaml
from flask import jsonify

import cmenv.config as config

def search():
    return jsonify(config.apis)
