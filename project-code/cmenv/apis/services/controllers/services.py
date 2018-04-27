import yaml
from flask import jsonify

import cmenv.config as config

def search():
    return jsonify({'running services': config.apis})
    
def put(name):
    return jsonify({'enabled': config.add_service(name)})
    
def delete(name):
    return jsonify({'disabled': config.remove_service(name)})
