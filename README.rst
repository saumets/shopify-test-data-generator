Shopify Test Data Generator
---------------------------

*STDG* is a Python package that automates the generation of test/fake data for any Shopify store. Are you developing a new feature, service, and/or plugin, but need some data in a store to actually help you with your testing? Then
STDG may be for you! Save yourself the hassle of manually creating all that Shopify store data through the dashboard. You need STDG.

STDG is dependent on the following packages: `ShopifyAPI`_, and `Faker`_

----

**Note**: This package is currently in a sandbox state. While usable, presently it's restricted to command-line usage only. This README file *may* be out of date at any time and further configuration may be required and/or necessary. 

----

Basic Setup
-----------

1. First get a python *virtualenv* up and running and clone the repo. Then:

.. code:: bash

    python setup.py develop
    
# Open and edit the provided *stdg-sample.ini* file and add your Shopify API credentials and optional settings.
# Save your above edits as *stdg.ini*.

Basic Usage
-----------

Simple help:

.. code:: bash

    stdg -h

Help on creating orders:

.. code:: bash

    stdg orders -h

Create 3 orders:

.. code:: bash

    stdg orders create 3

Create 2 customers:

.. code:: bash

    stdg customers create 2

Delete all generated orders:

.. code:: bash

    stdg orders delete

Delete all generated customers:

.. code:: bash

    stdg customers delete

.. _ShopifyAPI: https://github.com/Shopify/shopify_python_api
.. _Faker: https://github.com/joke2k/faker
