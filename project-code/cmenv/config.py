import os

import yaml

import cmenv.constants as constants

with open('config.' + constants.YAML_EXTENSION, 'r') as f:
    config = yaml.load(f)
    
if config['apis'] == 'all':
    apis = [d for d in os.listdir(constants.API_DIR)]
else:
    apis = config['apis']

