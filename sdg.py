#!/usr/bin/env python

import sys
import argparse
#import configparser

#import shopify
#import config
import resources

__author__ = 'paulsaumets'

def run():

    parser = argparse.ArgumentParser(prog='sdg', description='Auto-generate Shopify data for application testing.')
    subparsers = parser.add_subparsers(help='sub-command help', dest='sub_command')

    parser_customers = subparsers.add_parser('customers', help='generate customer data')
    parser_products = subparsers.add_parser('products', help="generate product data")

    parser_orders = subparsers.add_parser('orders', help='generate order data')
    parser_orders.add_argument('N', type=int,help='number of orders to generate')
    #parser_orders.set_defaults(func=resources.orders.generate)

    args = parser.parse_args()

    orders = resources.Orders(250)

    print(args)

    if args.sub_command == "orders":
        print('The N is %s' % (args.N))

    return

run()

# clean exit
sys.exit(0)
