#!/usr/bin/env python3

""" Basic command line tool for Hello World. """

import pyTemplateBath as tb
from pyTemplateBath._version import __version__
import pyCommonTools as pct
import argparse
import logging

def main():

    parser = pct.make_parser(prog='pyTemplateBath', version=__version__)

    base_args = pct.get_base_args()
    subparser = pct.make_subparser(parser)
    input_arg = pct.get_in_arg()

    qc_arg = argparse.ArgumentParser(add_help=False)
    qc_arg.add_argument(
        '--qc', metavar='FILE', help='Output file for QC statistics.')

    # Sub-parser
    sub_parser = subparser.add_parser(
        'hello',
        description=tb.hello.__doc__,
        help='Classic Hello World program.',
        parents=[base_args],
        epilog=parser.epilog)
    sub_parser.add_argument(
        '-n', '--name', default='World',
        help='Provide name. (default: %(default)s)')
    sub_parser.set_defaults(function=tb.hello.hello_world)

    read_parser = subparser.add_parser(
        'read',
        description=tb.read.__doc__,
        help='Output file.',
        parents=[base_args, input_arg, qc_arg],
        epilog=parser.epilog)
    read_parser.set_defaults(function=tb.read.read)

    return (pct.execute(parser))
