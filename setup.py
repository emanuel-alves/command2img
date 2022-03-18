# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
    
setup(
    name='command2img',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Emanuel Alves',
    author_email='emanuel.alves@unifei.edu.br',
    url='https://github.com/emanuel-alves/command2img',
    license=license,
    packages=find_packages()
)