import pytest
@pytest.mark.smoke
def test_firstProgram1():
    msg = "Hello"
    assert msg == "Hello", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"