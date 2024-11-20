import inspect

import pytest
from pytestDemo.BaseClass import BaseClass

pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editprofile(self, dataLoad):
        log = self.getLogger(inspect.stack()[0][3])
        log.info(dataLoad)
