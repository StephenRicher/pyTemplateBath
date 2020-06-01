#!/usr/bin/env python3

""" Print Hello World."""

import logging

def hello_world(name='World', **kwargs):

    print(f'Hello {name}.')
    logging.debug(f"Printed 'Hello {name}.'")
