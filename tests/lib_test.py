# tests/lib_test.py
from mytoolbox.lib import addition_function

def test_addition_function():
    assert len(addition_function(1,2)) == 3