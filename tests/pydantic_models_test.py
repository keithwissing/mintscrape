import json
import sys

import pytest

from src.models import ModelItem

def test_account_model() -> None:
    with open('data/account_data.json', 'r') as file:
        line = file.readline()
    accounts = [ModelItem(**x) for x in json.loads(line)]
    assert len(accounts) == 53

if __name__ == "__main__":
    sys.exit(pytest.main(["-q"]))
