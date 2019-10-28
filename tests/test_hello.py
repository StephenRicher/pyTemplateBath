import pytest
import pyTemplateBath as tb
import pyCommonTools as pct


def test_hello_world(capsys):
    
    """ Compare stdout with expected value. """
    
    tb.hello.hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World.\n"

def test_data(pct.datadir):
    
    """ Compare line by line, with expected data file. """
    
    expected_data = pct.datadir.join('test.dat')
    with open(expected_data) as f:
        for line in ['line1', 'line2']:
            assert f.readline().strip('\n') == line
