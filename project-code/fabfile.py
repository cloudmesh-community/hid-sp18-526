import os

import yaml
from fabric.api import local

import cmenv.config as config
import cmenv.constants as constants

def deploy():
    ubuntu_packages = []
    pip_packages = []

    for directory in os.listdir(constants.API_DIR):
        if directory in config.apis:
            up_file = constants.API_DIR + directory + '/packages.txt'
            pp_file = constants.API_DIR + directory + '/requirements.txt'
            
            if os.path.isfile(up_file):
                with open(up_file, 'r') as f:
                    ubuntu_packages += f.read().splitlines()
                    
            if os.path.isfile(pp_file):
                with open(pp_file, 'r') as f:
                    pip_packages += f.read().splitlines()

    if ubuntu_packages:                
        local('apt-get install ' + ' '.join(ubuntu_packages))
    
    if pip_packages:
        local('pip3 install ' + ' '.join(pip_packages))
