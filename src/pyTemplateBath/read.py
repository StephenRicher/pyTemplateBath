#!/usr/bin/env python3

""" Read a file."""

import sys
import pyCommonTools as pct
from contextlib import ExitStack

def read(infile=None, qc=None):

    log = pct.create_logger()

    with ExitStack() as stack:
        input = stack.enter_context(pct.open(infile))
        qc = stack.enter_context(pct.open(qc, stderr=True, mode='w'))

        for n, line in enumerate(input):
            sys.stdout.write(line)
        qc.write(f'Number of lines: {n}\n')
