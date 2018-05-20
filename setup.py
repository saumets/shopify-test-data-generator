#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = io.open(os.path.join(cwd, 'README.rst'), encoding="utf-8").read()

setup(name='stdg',
      version='0.0.1',
      description='STDG is a package that automates generation of Shopify store data for application testing purposes.',
      long_description=DESCRIPTION,
      entry_points={
          'console_scripts': ['stdg = stdg.cli:command_line_run']
      },
      url='https://github.com/skalfyfan/shopify-test-data-generator',
      author='Paul Saumets',
      author_email='ps@everydaybloke.com',
      license='MIT',
      packages=['stdg'],
      install_requires=[
          'ShopifyAPI',
          'Faker',
          'pandas'
      ],
      zip_safe=False)
