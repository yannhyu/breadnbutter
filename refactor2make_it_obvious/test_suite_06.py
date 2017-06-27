# test_suite_06.py
# easier to write test code
from func_evolves_into_class_05 import OystersGood

def test_oystergood_01():
    test = OystersGood('November')
    assert test
    assert test.r
    assert not test.ary

def test_oystergood_02():
    test = OystersGood('July')
    assert not test
    assert not test.r
    assert not test.ary