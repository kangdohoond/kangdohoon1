import pytest 

def test_file1_method1():
    x= 5
    y =6
    assert x+1 == y, "test failed"    # 저 조건이 아니라면 저 문장이 뜸
    assert x==y , "test failed"

def test_file1_method2():
    x=5
    y=6
    assert x+1 == y , "test failed"
