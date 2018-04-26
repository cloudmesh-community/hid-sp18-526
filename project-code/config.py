import os

import yaml

import constants

with open('config.' + constants.YAML_EXTENSION, 'r') as f:
    config = yaml.load(f)
    
if config['apis'] == 'all':
    apis = [d for d in os.listdir('apis')]
else:
    apis = config['apis']
