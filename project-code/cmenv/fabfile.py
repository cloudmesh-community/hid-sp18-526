import os

import yaml
from fabric.api import local

import cmenv.config as config
import cmenv.constants as constants

def deploy():
    local('mkdir ' + constants.DATA_DIRECTORY)

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
                with open(pp_file, 'r') as f:
                    pip_packages += f.read().splitlines()

    if ubuntu_packages:                
        local('apt-get install ' + ' '.join(ubuntu_packages))
    
    if pip_packages:
        local('pip3 install ' + ' '.join(pip_packages))