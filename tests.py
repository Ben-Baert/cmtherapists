import pytest
import helpers

def test_is_name():
    assert helpers.is_name("FARESA - Rue Joseph Stevens 7") is False
