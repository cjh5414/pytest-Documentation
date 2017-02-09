import pytest

def f():
    a = ['x', 'y']
    print(a[2])

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
