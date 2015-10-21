#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = io.open(os.path.join(cwd, 'README.md'), encoding="utf-8").read()

setup(name='shopify test data generator',
      version='0.1',
      description='STDG is a Python package that automates generation of Shopify store test data.',
      long_description=DESCRIPTION,
      entry_points= {
          'console_scripts': ['stdg = stdg.cli:command_line_run']
      },
      url='https://github.com/skalfyfan/shopify-test-data-generator',
      author='Paul Saumets',
      author_email='ps@everydaybloke.com',
      license='MIT',
      packages=['stdg'],
      install_requires=[
          'ShopifyAPI',
          'fake-factory'
      ],
      zip_safe=False)
