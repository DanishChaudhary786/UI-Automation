# Any pytest file should start with test_ or end with _test
# Pytest method name should start with test_
# Any code should be wrapped inside method only
import pytest


@pytest.mark.smoke
def test_CreditCard():
    print("Hello")
