#!/usr/bin/env python3

""" Read a file."""

import sys
import fileinput

def read(file, **kwargs):

    with fileinput.input(file) as fh:
        for n, line in enumerate(fh):
            sys.stdout.write(line)
