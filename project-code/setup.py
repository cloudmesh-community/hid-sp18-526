#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name = 'cmenv',
    version = '0.0.1',
    description = 'Deployable API Containers',
    url = 'https://github.com/cloudmesh-community/hid-sp18-526',
    author = ['Tim Whitson', 'Gregor von Laszewski'],
    author_email = 'whitstd@gmail.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = required,
    entry_points = {
        'console_scripts': [
            'cmenv = cmenv.__main__:main'
        ]
    })
