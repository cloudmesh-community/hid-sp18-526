import os
from subprocess import run

import yaml

import cmenv.config as config
import cmenv.constants as constants

if not os.path.exists(constants.DATA_DIR):
    os.mkdir(constants.DATA_DIR)

ubuntu_packages = []
pip_packages = []

for directory in os.listdir(constants.API_DIR):
    if directory in config.apis:
        up_file = constants.API_DIR + '/' + directory + '/packages.txt'
        pp_file = constants.API_DIR + '/' + directory + '/requirements.txt'
        
        if os.path.isfile(up_file):
            with open(up_file, 'r') as f:
                ubuntu_packages += f.read().splitlines()
                
        if os.path.isfile(pp_file):
            with open(pp_file, 'r') as f:
                pip_packages += f.read().splitlines()

if ubuntu_packages:                
    run(['apt-get', 'install'] + ubuntu_packages)

if pip_packages:
    run(['pip3', 'install'] + pip_packages)
