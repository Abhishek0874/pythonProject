"""
pytest_demo is framework for test in python selenium automation
#Selenium Python Framework Design Plan :
# 1 Pytest Unit Testing Framework
# 2 Understanding Logging and HTML Reports
# 3 Implement Selenium Python Framework from Scratch(Page Object Design Pattern)
# 4 Data Driven Framework with Excel to Selenium Python Tests
# 5 GIT Version Control

# Pytest Unit Testing Framework :
#pytestdel file should start with test_
#pytestdel method names should strat with test
#Any code should be wrapped in method only
#in py test every method is treated as a test case
#cmd command : --v to check the pytestversion from cmd window
#cmd command : py.test -v -s (to run pytestdel from cmd window, this command runs all
 the files in the present folder)
#to run a selected file cmd command : py.test filename -v -s (eg: py.test test_tenth_demo.py -v -s)
#py.test -k CreditCard -v -s : to run selected module test cases from different files
 with partial or common functionName/Module between them(as CreditCard is
 common between 2 test cases/module)
#method name should have sense
# -k stands for method names execution
# -s stands for logs in output
# -v stands for more info metadata
# you can mark/tag tests @pytest.mark.smoke and then run with py.test -m smoke -v -s
 in @pytest_demo.mark.smoke (smoke can be any name according to the naming convention)
# @pytest.mark.skip : (to skip a test)
# @pytest.mark.xfail : (to run but not to report in the output)

"""
import pytest
#@pytest.mark.smoke # to mark a testcase
@pytest.mark.skip #to skip a selected test case
def test_firstProgram():
    print("Hello Abhishek")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")
