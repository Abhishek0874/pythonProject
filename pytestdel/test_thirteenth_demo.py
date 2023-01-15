import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editprofile(self, dataLoad):
        print(dataLoad) #to print the whole data that is ["Abhishek", "Gaikwad", "abhishek.gaikwad082gmail.com"]
        print(dataLoad[0]) #to print the 0th index tuple that is Abhishek
        print(dataLoad[1]) #to print the 0th index tuple that is Gaikwad

"""
conftest file for above program from the fixture data is being called:
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Abhishek", "Gaikwad", "abhishek.gaikwad082gmail.com"]
"""












