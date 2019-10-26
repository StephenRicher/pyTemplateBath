#!/usr/bin/env python3

import pyTemplateBath.hello
import pyCommonTools as pct
import sys
import argparse
import logging


def main():

    epilog = 'Stephen Richer, University of Bath, Bath, UK (sr467@bath.ac.uk)'

    formatter_class = argparse.ArgumentDefaultsHelpFormatter

    parser = argparse.ArgumentParser(
        prog='pyTemplateBath',
        description=__doc__,
        formatter_class=formatter_class,
        epilog=epilog)

    subparsers, base_args = pct.set_subparser(parser)

    # Sub-parser
    sub_parser = subparsers.add_parser(
        'hello',
        description=pyTemplateBath.hello.__doc__,
        help='Classic Hello World program.',
        parents=[base_args],
        formatter_class=formatter_class,
        epilog=epilog)
    sub_parser.add_argument(
        '-n', '--name', default='World',
        help='Provide name.')
    sub_parser.set_defaults(function=pyTemplateBath.hello.hello_world)

    args = parser.parse_args()

    log = pct.create_logger(
        initialise=True,
        output=args.log,
        level=logging.DEBUG if args.verbose else None)

    try:
        func = args.function
    except AttributeError:
        parser.print_help()
        sys.exit()

    args_dict = vars(args)

    [args_dict.pop(key) for key in ['command', 'function', 'verbose', 'log']]

    return func(**vars(args))
