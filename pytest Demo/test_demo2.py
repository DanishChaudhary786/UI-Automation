# Method name should have sense
#     -k stands for method names execution, -s logs in output, -v stands for more info metadata
# You can run specific with py.test filename
# you can mark (tag) @pytest.mark.smoke and then run with -m
# You can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - confest file to generalize
# fixture and make it available to all test cases
import pytest


@pytest.mark.xfail
def test_secondProgram():
    msg = "dc"
    assert msg == "hi", "Test failed as expected"


@pytest.mark.skip
def test_thirdCreditCard():
    a = 4
    b = 6
    assert a + b == 10, "Addition failed as expected"


@pytest.mark.usefixtures("setup")
def test_fixtureDemo():
    print("I will execute steps in the fixtureDemo method")
