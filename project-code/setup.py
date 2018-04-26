import os
from setuptools import setup

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()
 
# recursive package definition
# from user: Sandy Chapman, https://stackoverflow.com/a/36693250
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('cmenv/apis')

setup(
    name = 'cmenv',
    version = '0.0.1',
    description = 'Deployable API Containers',
    url = 'https://github.com/cloudmesh-community/hid-sp18-526',
    author = ['Tim Whitson', 'Gregor von Laszewski'],
    author_email = 'whitstd@gmail.com',
    license = 'MIT',
    packages = ['cmenv'],
    package_data={'': extra_files},
    install_requires = required,
    entry_points = {
        'console_scripts': [
            'cmenv = cmenv.__main__:main'
        ]
    }
)
