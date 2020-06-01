#!/usr/bin/env python3

""" Basic command line tool for Hello World. """

import pyTemplateBath as tb
import sys
import logging
import argparse
from ._version import __version__


def parse_arguments():

    epilog='Stephen Richer, University of Bath, Bath, UK (sr467@bath.ac.uk)'

    version = argparse.ArgumentParser(add_help=False)
    version.add_argument(
        '--version', action='version', version=f'%(prog)s {__version__}')
    verbose = argparse.ArgumentParser(add_help=False)
    verbose.add_argument(
        '--verbose', action='store_const', const=logging.DEBUG,
        default=logging.INFO, help='verbose logging for debugging')

    parser = argparse.ArgumentParser(
        epilog=epilog, description=__doc__, parents=[version])
    subparser = parser.add_subparsers(
        title='required commands',
        description='',
        dest='command',
        metavar='Commands',
        help='Description:')

    hello = subparser.add_parser(
        'hello',
        description=tb.hello.__doc__,
        help='Classic Hello World program.',
        parents=[version, verbose],
        epilog=parser.epilog)
    hello.add_argument(
        '--name', default='World',
        help='Provide name. (default: %(default)s)')
    hello.set_defaults(function=tb.hello.hello_world)

    read = subparser.add_parser(
        'read',
        description=tb.read.__doc__,
        help='Output file.',
        parents=[version, verbose],
        epilog=parser.epilog)
    read.add_argument(
        'file', metavar='FILE', nargs='?', default=[],
        help='Input file (default: stdin)')
    read.set_defaults(function=tb.read.read)

    args = parser.parse_args()
    if 'function' not in args:
        parser.print_help()
        sys.exit()

    log_format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level=args.verbose, format=log_format)

    return args
