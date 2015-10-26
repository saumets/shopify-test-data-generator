import shopify
from faker import Factory
from pyactiveresource.connection import ResourceNotFound

import pandas as pd

from stdg import config

class Customers(object):

    settings = config.settings['customers']

    def __init__(self, locale="en_US"):

        self.locale = locale

        postal_data = pd.read_csv("zip-codes.txt")
        postal_data.columns = ["postal_code", "lat", "long", "city", "state", "county", "unique"]

        self.states = list(postal_data.state)
        self.zips = list(postal_data.postal_code)


        return

    # class methods

    def generate_data(self):

        # We're forcing US locale since it contains the most complete providers for the Faker package.
        fake = Factory.create(self.settings['LOCALE'])

        first_name = fake.first_name()
        last_name = fake.last_name()

        state = fake.state_abbr()
        # get a valid zip base on the chosen state

        state_index = self.states.index(state)
        postal_code = self.zips[state_index]

        #print(state)
        #print(postal_code)

        customer = {
            'first_name': first_name,
            'last_name': last_name,
            'addresses': [
                {
                    'address1': fake.street_address(),
                    'city': fake.city(),
                    'province_code': str(state),
                    'phone': fake.phone_number(),
                    'zip': str(postal_code),
                    'last_name': first_name,
                    'first_name': last_name,
                    'country': 'US'
                }
            ],
        }

        return customer

    # instance methods

    def create(self, number_customers):

        customers_created = []

        for counter in range(number_customers):

            print("Generating Customer: {0}".format(str(counter+1)))

            new_customer = shopify.Customer().create(self.generate_data())

            if new_customer.errors:
                # something went wrong!
                # TODO: we need to loop over our error messages and print them
                for message in new_customer.errors.full_messages():
                    print(message)
                return

            customers_created.append(str(new_customer.id))

        with open('stdg-customers.csv', mode='a', encoding='utf-8') as customers_file:
            customers_file.write('\n'.join(customers_created) + '\n')

        return

    def delete(self, customers=None):

        if customers is None:
            # delete all orders
            with open('stdg-customers.csv') as customer_file:
                customers_delete = customer_file.read().splitlines()

            for customer_id in customers_delete:

                try:
                    customer = shopify.Customer.find(int(customer_id))
                    customer.destroy()
                    print("[DELETED] Customer #{0}".format(customer_id))
                except ResourceNotFound:
                    print("[WARNING]: Customer #{0} not found.".format(customer_id))
                except:
                    print("Customer #: {0} has existing orders maybe?".format(customer_id))

        return
