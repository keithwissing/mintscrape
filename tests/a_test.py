import sys
from unittest import IsolatedAsyncioTestCase

import pytest

def test_nothing() -> None:
    assert True

class Test(IsolatedAsyncioTestCase):
    async def test_no_data(self):
        assert True

if __name__ == "__main__":
    sys.exit(pytest.main(["-q"]))
