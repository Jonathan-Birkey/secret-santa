#!/usr/bin/env python3
__author__ = 'Jonathan Birkey'
__email__ = 'jonathan.birkey@gmail.com'
__date__ = '05May2022'

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='secret-santa',
    version='0.1.0',
    description='Randomly pick names and email everyone their secret santa',
    long_description=readme,
    author=__author__,
    author_email=__email__,
    url='https://github.com/Jonathan-Birkey/secret-santa',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "click == 8.1.3",
        "mysql"
    ],
    entry_points='''
        [console_scripts]
        santa=secretsanta:main
    '''
)
