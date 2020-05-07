
#!/usr/bin/env python3

import pytest
import pyTemplateBath as tb
from pyCommonTools import datadir

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

    steamOutput = {'stdout': {'expected': datadir.join(expectedStdout),
                              'observed': captured.out.splitlines(True)},
                   'stderr': {'expected': datadir.join(expectedStderr),
                              'observed': captured.err.splitlines(True)}}

    for stream in ['stdout', 'stderr']:
        expectedFile = steamOutput[stream]['expected']
        observedOut = steamOutput[stream]['observed']
        with open(expectedFile) as expectedOut:
            for observedLine, expectedLine in zip(observedOut, expectedOut):
                assert observedLine == expectedLine
