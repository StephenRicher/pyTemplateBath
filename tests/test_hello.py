#!/usr/bin/env python3

import os
import pytest
import pyTemplateBath as tb
from distutils import dir_util

hello_word_params = (
    [('default.out', 'default.err', None),
     ('name1.out', 'name1.err', 'Stephen')])

@pytest.mark.parametrize(
    'expectedStdout, expectedStderr, name', hello_word_params)
def test_hello_world(expectedStdout, expectedStderr, name, datadir, capsys):
    """ Compare stdout and stderr against expected output """

    # Run test function
    if name is None:
        tb.hello.hello_world()
    else:
        tb.hello.hello_world(name)

    # Capture stdout/stderr of test function
    captured = capsys.readouterr()

    streamOutput = {'stdout': {'expected': datadir.join(expectedStdout),
                               'observed': captured.out.splitlines(True)},
                    'stderr': {'expected': datadir.join(expectedStderr),
                               'observed': captured.err.splitlines(True)}}

    for stream in ['stdout', 'stderr']:
        expectedFile = streamOutput[stream]['expected']
        observedOut = streamOutput[stream]['observed']
        with open(expectedFile) as expectedOut:
            for observedLine, expectedLine in zip(observedOut, expectedOut):
                assert observedLine == expectedLine


@pytest.fixture
def datadir(tmpdir, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely. datadir can be used just like tmpdir.
    '''

    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir
