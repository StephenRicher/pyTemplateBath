import pyTemplateBath.hello
import pytest

def test_run():
    assert pyTemplateBath.hello.hello_world()
