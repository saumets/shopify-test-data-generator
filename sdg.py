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


    subparsers = parser.add_subparsers(dest='primary_command')
    parser_orders = subparsers.add_parser('orders', help='generate order data')
    parser_customers = subparsers.add_parser('customers', help='generate customer data')
    parser_products = subparsers.add_parser('products', help="generate product data")

    order_subparser = parser_orders.add_subparsers(dest='secondary_command')
    order_create_subparser = order_subparser.add_parser('create', help="create orders")
    order_delete_subparser = order_subparser.add_parser('delete', help="delete orders")

    # order secondary_command arguments
    order_create_subparser.add_argument('N', type=int, help='number of orders to create (integer)')

    args = parser.parse_args()

    if args.primary_command == "orders":
        orders = resources.Orders(250)

        if args.secondary_command == "create":
            orders.create(args.N)

        if args.secondary_command == "delete":
            orders.delete_orders()

    print("Process Completed.\n")
    return

run()

# clean exit
sys.exit(0)
