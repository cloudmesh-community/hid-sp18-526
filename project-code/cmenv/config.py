import os

import yaml

import cmenv.constants as constants

with open('config.' + constants.YAML_EXTENSION, 'r') as f:
    config = yaml.load(f)
    
if config['apis'] == 'all':
    apis = [d for d in os.listdir(constants.API_DIR)]
    config['apis'] = apis
else:
    apis = config['apis']
    
def add_service(name):
    if name not in config['apis']:
        config['apis'] += [name]
        save()
        return True
    else:
        return False
    
def remove_service(name):
    try:
        config['apis'].remove(name)
        save()
        return True
    except:
        return False
    
def save():
    with open('config.' + constants.YAML_EXTENSION, 'w+') as f:
        yaml.dump(config, f, default_flow_style = False)

