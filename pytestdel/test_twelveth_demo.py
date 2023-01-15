
import pytest

def test_fixtureDemo1(setup):
    print("i will execute steps in fixtureDemo method")


"""
conftest file program :
import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")
"""
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo method")


    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo1 method")


    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo2 method")


    def test_fixtureDemo4(self):
        print("i will execute steps in fixtureDemo3 method")

"""
In conftest  if u use scope = "class"
(import pytest


@pytest.fixture(scope = "class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")
)
u will get he fixture recalled only at the start and end.
"""



























