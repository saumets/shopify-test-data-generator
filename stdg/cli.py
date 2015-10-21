# coding=utf-8

import sys
import argparse

import resource

__author__ = 'paulsaumets'


def command_line_run():
    # make sure at least one argument was passed before we jump into argparse
    if not len(sys.argv) > 1:
        print("usage: sdg [-h] [--version] {orders,customers,products} ...")
        return

    parser = argparse.ArgumentParser(prog='sdg', description='Automate generation of Shopify test data for application testing.')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    subparsers = parser.add_subparsers(dest='primary_command')
    parser_orders = subparsers.add_parser('orders', help='generate order data')
    parser_customers = subparsers.add_parser('customers', help='generate customer data')
    parser_products = subparsers.add_parser('products', help="generate product data")

    order_subparser = parser_orders.add_subparsers(dest='secondary_command')
    order_create_subparser = order_subparser.add_parser('create', help="create orders")
    order_delete_subparser = order_subparser.add_parser('delete', help="delete orders")

    customer_subparser = parser_customers.add_subparsers(dest='secondary_command')
    customer_create_subparser = customer_subparser.add_parser('create', help="create customers")
    customer_delete_subparser = customer_subparser.add_parser('delete', help="delete customers")

    # orders secondary_command arguments
    order_create_subparser.add_argument('N', type=int, help='number of orders to create (integer)')

    # customers secondary_command arguments
    customer_create_subparser.add_argument('N', type=int, help='number of customers to create (integer)')

    args = parser.parse_args()

    if args.primary_command == "orders":
        orders = resource.Orders(limit_sample_size=250)

        if args.secondary_command == "create":
            orders.create(args.N)

        if args.secondary_command == "delete":
            orders.delete()

    if args.primary_command == "customers":
        customers = resource.Customers()

        if args.secondary_command == "create":
            customers.create(args.N)

        if args.secondary_command == "delete":
            customers.delete()

    print("Process Completed.\n")
    return
