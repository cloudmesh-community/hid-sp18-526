import os

import yaml
import connexion
from fabric.api import local

from document import APIDoc
from resolver import CMResolver
import constants

with open('config.' + constants.YAML_EXTENSION, 'r') as f:
    config = yaml.load(f)
    
if config['apis'] == 'all':
    config['apis'] = [d for d in os.listdir('apis')]

def deploy():
    ubuntu_packages = []
    pip_packages = []

    for directory in os.listdir('apis'):
        if directory in config['apis']:
            up_file = 'apis/' + directory + '/packages.txt'
            pp_file = 'apis/' + directory + '/requirements.txt'
            
            if os.path.isfile(up_file):
                with open(up_file, 'r') as f:
                    ubuntu_packages += f.read().splitlines()
                    
            if os.path.isfile(pp_file):
                with open(up_file, 'r') as f:
                    pip_packages += f.read().splitlines()
                        
    local('apt-get install ' + ' '.join(ubuntu_packages))
    local('pip install ' + ' '.join(pip_packages))
    
def run():
    doc = APIDoc(
        title = 'yolo',
        version = '1.0',
        swagger = '2.0'
    )

    controller_dispatch = doc.set_apis(config['apis'])

    app = connexion.App(__name__)
    app.add_api(doc.to_dict(), resolver = CMResolver(controller_dispatch))
    app.run(port = 8080)
