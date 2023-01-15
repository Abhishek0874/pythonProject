"""
#Fixtures :
Fixture is used as pre-requisite
A fixture if u know is shared by multiple files u can store it in conftest.py file
Then every time u call a fixture it will see the conftest file if a fixture is availble and recall,
it  in your file
So u dont need to give ur common fixture evrytime is every of ur file u can just recall it.
Fixtures are used as setup and tear down methods for test cases -conftest file to generaalize,
fixture and make it available to all test cases.
(Note : The name of the fixture function can later be referenced to cause its invocation ahead,
 of running tests: test modules or classes can use the pytest.mark.usefixtures(fixturename) marker.
Test functions can directly use fixture names as input arguments in which case the fixture instance
returned from the fixture function will be injected.
Fixtures can provide their values to test functions using return or yield statements.
When using yield the code block after the yield statement is executed as teardown code regardless of
the test outcome, and must yield exactly once.)
conftest file is created between file 11th and 12th.
Through fixture u can load the data , in the fixture u can load the data,
and then pass the data to ur test throuht the fixture.
Datadriven and parameterization can be done withreturn statements in tuple format.
when u define fixture scope to class only, it will run once before class is initiated and at the end.
"""
"""
Studied topics :
Naming conventions to follow for pytest ?
Running pytest from cmd and pycharm ?
Pytest tags mechanism to run tests based on functionality ?
Failing and skipping tests with annotations using Pytest ?
What arefixtures and imp of their hooks in Pytest ?
How fixtures can be configured in conftest file for better readeability ?
Different scope of fixtures and their related annotations to setup Pre and Post conditions of test ?
How parameterization can be achieved for Tests with multiple sets of data
How to pass cmd line arguments into Pytests ?
HTML report generations for pytest execution ?
"""
import pytest
@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello Abhishek")


@pytest.mark.xfail
def test_SecondGreetCreditCard(setup):
    print("Good Morning")











