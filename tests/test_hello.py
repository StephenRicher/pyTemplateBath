import pyTemplateBath.hello
import pytest
import pyCommonTools.logging

def test_run():
    assert pyTemplateBath.hello.hello_world()

def test_install_requires():
    assert hasattr(pyCommonTools.logging.create_logger, '__call__')
