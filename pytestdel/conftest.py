import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Abhishek", "Gaikwad", "abhishek.gaikwad082gmail.com"]


@pytest.fixture(params=[("chrome", "Abhishek", "Gaikwad"), ("Firefox", "Abhi"), ("IE", "Tester")])
def crossBrowser(request):
    return request.param