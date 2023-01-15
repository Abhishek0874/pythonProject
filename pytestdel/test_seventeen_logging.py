import pytest
import logging
from pytestdel.test_sixteen_logging import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editprofile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])


"""
log-file output-
2023-01-09 07:19:41,027 : INFO : test_editprofile : Abhishek
2023-01-09 07:19:41,027 : INFO : test_editprofile : abhishek.gaikwad082gmail.com
"""