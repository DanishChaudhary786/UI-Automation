# Method name should have sense
#     -k stands for method names execution, -s logs in output, -v stands for more info metadata
# You can run specific with py.test filename
# you can mark (tag) @pytest.mark.smoke and then run with -m
# You can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - confest file to generalize
# fixture and make it available to all test cases
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    @pytest.mark.xfail
    def test_secondProgram(self):
        self.msg = "dc"
        assert self.msg == "dc", "Test failed as expected"

    def test_thirdCreditCard(self):
        a = 4
        b = 6
        assert a + b == 10, "Addition failed as expected"

    def test_fixtureDemo(self):
        print("I will execute steps in the fixtureDemo method")
