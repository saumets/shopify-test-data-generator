import random
import shopify

from pyactiveresource.connection import ResourceNotFound

from stdg import config
from stdg.resource.customers import Customers


class Orders(object):

    settings = config.settings['orders']

    def __init__(self, limit_sample_size=250):

        # retains the max product sample size from which to create orders
        self.products = shopify.Product.find(limit=limit_sample_size)

        return

    # class methods

    def generate_data(self, cls):

        customer = Customers()

        customer_data = customer.generate_data()

        order = {
            'customer': customer_data,
            'shipping_address': {
                'first_name': customer_data['first_name'],
                'last_name': customer_data['last_name'],
                'phone': customer_data['addresses'][0]['phone'],
                'address1': customer_data['addresses'][0]['address1'],
                'city': customer_data['addresses'][0]['city'],
                'province_code': customer_data['addresses'][0]['province_code'],
                'zip': customer_data['addresses'][0]['zip'],
                'country': 'US'
            },
            'line_items': cls.line_items_create()
        }

        return order

    def line_items_create(self):

        line_items = []

        # how many different products can a single customer order?
        sample_size = random.randint(1, int(self.settings['MAX_LINE_ITEMS']))

        # get a random # of products (aka line_items) for this purchase.
        products = random.sample(self.products, sample_size)
        print("Total Products Purchased In Order: {}\n".format(len(products)))

        for product in products:
            if len(product.variants) < int(self.settings['MAX_VARIANTS']):
                variants = product.variants
            else:
                # generate a random seed to how big our sample size should be
                sample_size = random.randint(1, int(self.settings['MAX_VARIANTS']))
                variants = random.sample(product.variants, sample_size)

            for variant in variants:
                line_items.append(
                    dict(id=product.id, variant_id=variant.id,
                         quantity=random.randint(1, int(self.settings['MAX_QUANTITY'])),
                         fulfillment_service=self.settings['FULFILLMENT_SERVICE'], fulfillment_status=self.settings['FULFILLMENT_STATUS'])
                )



        return line_items


    # instance methods

    def create(self, number_orders):

        # these lists will be added to a data file after creation
        orders_created = []
        customers_created = []

        print("Total Products Sampling From: {}\n".format(len(self.products)))

        for counter in range(number_orders):

            print("Generating Order: {0}".format(str(counter + 1)))

            new_order = shopify.Order().create(self.generate_data(self))

            if new_order.errors:
                # something went wrong!
                # TODO: we need to loop over our error messages and print them
                for message in new_order.errors.full_messages():
                    print("[ERROR] {0}".format(message))
                return

            orders_created.append(str(new_order.id))
            customers_created.append(str(new_order.customer.id))

        # Write our created data to file. This is required for simple deletion later using this same tool.
        # If these files do not exist, you will have to delete the data manually through the Shopify dashboard.
        with open('stdg-orders.csv', mode='a', encoding='utf-8') as order_file:
            order_file.write('\n'.join(orders_created) + '\n')

        with open('stdg-customers.csv', mode='a', encoding='utf-8') as customers_file:
            customers_file.write('\n'.join(customers_created) + '\n')

        return

    def delete(self, orders=None):

        if orders is None:
            # delete all orders
            with open('stdg-orders.csv') as order_file:
                orders_delete = order_file.read().splitlines()

            for order_number in orders_delete:

                try:
                    order = shopify.Order.find(int(order_number))
                    order.cancel()
                    order.destroy()
                    print("[DELETED] Order #{0}".format(order_number))
                except ResourceNotFound:
                    print("[WARNING] Order #{0} not found.".format(order_number))

        return
