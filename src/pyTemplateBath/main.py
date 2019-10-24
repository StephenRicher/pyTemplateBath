#!/usr/bin/env python3

import pyTemplateBath.hello
import pyCommonTools.logging
import sys, argparse

def main():
    
    epilog = 'Stephen Richer, University of Bath, Bath, UK (sr467@bath.ac.uk)'

    formatter_class = argparse.ArgumentDefaultsHelpFormatter

    parser = argparse.ArgumentParser(
        prog = 'pyTemplateBath',
        description = __doc__,
        formatter_class = formatter_class,
        epilog = epilog)
        
    # Parent parser for options common to all sub commands.
    base_parser = argparse.ArgumentParser(
        formatter_class = formatter_class,
        add_help = False)
    base_parser.add_argument(
        '-v', '--verbose', 
        action = 'store_true',
        help = 'Verbose logging for debugging.')
    base_parser.add_argument(
        '-l', '--log', nargs = '?',
        help = 'Log output file.')
        
    # Define subparser
    subparsers = parser.add_subparsers(
        title = 'required commands',
        description = '',
        dest = 'command',
        metavar = 'Commands',
        help = 'Description:')
        
    # Sub-parser
    sub_parser = subparsers.add_parser('hello',
        description = pyTemplateBath.hello.__doc__,
        help = 'Classic Hello World program.', 
        parents = [base_parser],
        formatter_class = formatter_class,
        epilog = epilog)
    sub_parser.add_argument(
        '-n', '--name', default = 'World', 
        help = 'Provide name.')
    sub_parser.set_defaults(function = pyTemplateBath.hello.hello_world)
    
    args = parser.parse_args()
    
    try:
        func = args.function
    except AttributeError:
        parser.print_help()
        sys.exit()
    
    log = pyCommonTools.logging.create_logger()
    pyCommonTools.logging.initiliase_logger(
        log_output = args.log,
        log_level = logging.DEBUG if args.verbose else None)
    
    args_dict = vars(args)

    [args_dict.pop(key) for key in ['command', 'function', 'verbose', 'log']]
    
    return func(**vars(args))
