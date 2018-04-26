import os

import yaml
from fabric.api import local

import config

def deploy():
    ubuntu_packages = []
    pip_packages = []

    for directory in os.listdir('apis'):
        if directory in config.apis:
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
