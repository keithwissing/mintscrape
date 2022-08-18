import datetime
import json
import sys

import pytest

from src.basic import networth_to_influx, accounts_to_influx
from src.models import ModelItem, OlderAccount

def test_networth_to_influx() -> None:
    networth = 1234234
    timestamp = int(datetime.datetime(2022, 2, 3, 7, 1, 12).timestamp() * 1000000000)
    result = networth_to_influx(timestamp, networth)
    assert result == 'networth value=1234234 1643889672000000000'

def test_account_model() -> None:
    with open('data/account_data.json', 'r') as file:
        line = file.readline()
    accounts = [ModelItem(**x) for x in json.loads(line)]
    assert len(accounts) == 53

def test_account_to_influx() -> None:
    with open('data/account_data.json', 'r') as file:
        line = file.readline()
    accounts = [ModelItem(**x) for x in json.loads(line)]
    timestamp = int(datetime.datetime(2022, 2, 3, 7, 1, 12).timestamp() * 1000000000)
    result = accounts_to_influx(timestamp, accounts)
    for a in result:
        print(a)

def test_reading_all_history() -> None:
    count = 0
    with open('data/accounts_js.txt', 'r') as file:
        for line in file.readlines():
            date, time, data = line.split(maxsplit=2)
            data = json.loads(data)
            if 'klass' in data[0]:
                things = [OlderAccount(**x) for x in data]
            else:
                things = [ModelItem(**x) for x in data]
            count += 1

def test_reading_all_networth() -> None:
    with open('data/investments.txt', 'r') as file:
        for line in file.readlines():
            date, time, data = line.split(maxsplit=2)
            data = json.loads(data)
            assert isinstance(data, dict)

def test_reading_all_networth() -> None:
    with open('data/networth.txt', 'r') as file:
        for line in file.readlines():
            date, time, data = line.split(maxsplit=2)
            data = float(data)

if __name__ == "__main__":
    sys.exit(pytest.main(["-q"]))
