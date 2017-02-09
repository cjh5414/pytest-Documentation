import pytest


def test_zero_division():
     with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        pass
