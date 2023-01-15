
import pytest


def test_crossBrowser(crossBrowser):
    print(crossBrowser) #to print the whole output
    print(crossBrowser[1]) # to print the output with index 1

"""
conftest program for above test
@pytest.fixture(params=[("chrome", "Abhishek", "Gaikwad"), ("Firefox", "Abhi"), ("IE", "Tester")])
def crossBrowser(request):
    return request.param
"""
"""
To install pytest html - pipinstall pytest-html
To run your test with - pytest --html=report.html
"""












