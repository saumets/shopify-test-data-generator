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
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    #parser.add_argument('resource', choices=['customers','orders','products'], help="Resource CRUD interface")


    subparsers = parser.add_subparsers()
    parser_orders = subparsers.add_parser('orders', help='generate order data')
    parser_customers = subparsers.add_parser('customers', help='generate customer data')
    parser_products = subparsers.add_parser('products', help="generate product data")

    order_subparser = parser_orders.add_subparsers()
    order_create_subparser = order_subparser.add_parser('create', help="create orders")
    order_delete_subparser = order_subparser.add_parser('delete', help="delete orders")


    args = parser.parse_args()

    orders = resources.Orders(250)

    print(args)

    if args.sub_command == "orders":
        print('The N is %s' % (args.N))

    return

run()

# clean exit
sys.exit(0)
