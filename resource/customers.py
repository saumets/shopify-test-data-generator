import shopify
import config

from faker import Factory


class Customers:
    def __init__(self):
        return

    @staticmethod
    def create(locale="en_CA"):
        # create our factory for generating fake customer names
        fake = Factory.create(locale)

        customer = dict(first_name=fake.first_name(), last_name=fake.last_name())

        return customer
