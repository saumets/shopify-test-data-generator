import random
import shopify

import config

from faker import Factory


class Orders:

    def __init__(self, limit_sample_size):

        self.products = shopify.Product.find(limit=limit_sample_size)
        return

    def generate(self, number_products):

        print("Total Products: {}".format(len(self.products)))

        fake = Factory.create('en_CA')

        for counter in range(number_products):

            print("Generating Order: " + str(counter))
            new_order = shopify.Order()
            new_order.customer = dict(first_name=fake.first_name(), last_name=fake.last_name())
            new_order.line_items = self.line_items_generate()

            success = new_order.save()

            if new_order.errors:
                # something went wrong!
                print(new_order.errors.full_messages())

        return

    def line_items_generate(self):
        settings = config.settings['orders']
        line_items = []

        # how many different products can a single customer order?
        sample_size = random.randint(1, int(settings['MAX_LINE_ITEMS']))

        # get a random # of products (aka line_items) for this purchase.
        products = random.sample(self.products, sample_size)
        print("Total Random Products Grabbed: {}\n".format(len(products)))

        for product in products:
            if len(product.variants) < int(settings['MAX_VARIANTS']):
                variants = product.variants
            else:
                # generate a random seed to how big our sample size should be
                sample_size = random.randint(1, int(settings['MAX_VARIANTS']))
                variants = random.sample(product.variants, sample_size)

            for variant in variants:
                line_items.append(
                    dict(id=product.id, variant_id=variant.id,
                         quantity=random.randint(1, int(settings['MAX_QUANTITY'])))
                )

        return line_items
