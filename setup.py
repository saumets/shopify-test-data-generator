#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = io.open(os.path.join(cwd, 'README.md'), encoding="utf-8").read()

setup(name='shopify test data generator',
      version='0.1',
      description='SDG is a Python package that auto-generates Shopify store data which can be used for testing when developing apps.',
      long_description=DESCRIPTION,
      url='https://github.com/skalfyfan/shopify-data-generator',
      author='Paul Saumets',
      author_email='ps@everydaybloke.com',
      license='MIT',
      packages=['sdg'],
      install_requires=[
        'ShopifyAPI',
        'fake-factory'
      ],
      zip_safe=False)
