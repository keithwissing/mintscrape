import datetime
import json
from typing import List, Optional

import mintapi
import requests
from get_docker_secret import get_docker_secret
from pydantic.dataclasses import dataclass

from models import ModelItem

@dataclass
class Configuration:
    user_name: str
    password: str
    mfa_token: str

def get_configuration() -> Optional[Configuration]:
    uname = get_docker_secret('mint_username')
    passwd = get_docker_secret('mint_password')
    token = get_docker_secret('mint_mfa_token')
    if not uname or not passwd or not token:
        return None
    # influx_host = get_docker_secret('influx_host')
    # influx_db = get_docker_secret('influx_db')
    return Configuration(uname, passwd, token)

def get_data_from_mint():
    config = get_configuration()
    mint = mintapi.Mint(
        config.user_name,  # Email used to log in to Mint
        config.password,  # Your password used to log in to mint
        # Optional parameters
        mfa_method='soft-token',  # Can be 'sms' (default), 'email', or 'soft-token'.
        mfa_token=config.mfa_token,
        # if mintapi detects an MFA request, it will trigger the requested method
        # and prompt on the command line.
        headless=True,  # Whether the chromedriver should work without opening a
        # visible window (useful for server-side deployments)
        mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
        # which returns the user-inputted 2FA code. By default
        # the default Python `input` function is used.
        session_path='/data/session',  # Directory that the Chrome persistent session will be written/read from.
        # To avoid the 2FA code being asked for multiple times, you can either set
        # this parameter or log in by hand in Chrome under the same user this runs
        # as.
        imap_account=None,  # account name used to log in to your IMAP server
        imap_password=None,  # account password used to log in to your IMAP server
        imap_server=None,  # IMAP server host name
        imap_folder='INBOX',  # IMAP folder that receives MFA email
        wait_for_sync=True,  # wait for accounts to sync
        wait_for_sync_timeout=300,  # number of seconds to wait for sync
        use_chromedriver_on_path=True,  # True will use a system provided chromedriver binary that
        # is on the PATH (instead of downloading the latest version)
    )

    # Initiate an account refresh
    # mint.initiate_account_refresh()

    # Get net worth
    nw = mint.get_net_worth_data()

    # Get basic account information
    acc = mint.get_account_data()

    # Get extended account detail at the expense of speed - requires an
    # additional API call for each account
    # mint.get_accounts(True)

    # Get budget information
    # mint.get_budgets()

    # Get transactions
    # mint.get_transactions()  # as pandas dataframe
    # mint.get_transactions_csv(include_investment=False)  # as raw csv data
    # mint.get_transactions_json(include_investment=False, skip_duplicates=False)

    # Get transactions for a specific account
    # accounts = mint.get_accounts(True)
    # for account in accounts:
    #     mint.get_transactions_csv(id=account["id"])
    #     mint.get_transactions_json(id=account["id"])

    # Get credit score
    # mint.get_credit_score()

    # Get bills
    # mint.get_bills()

    # Get investments (holdings and transactions)
    inv = mint.get_invests_data()

    # Close session and exit cleanly from selenium/chromedriver
    mint.close()

    return nw, acc, inv

def remove_account_datetimes(account):
    DATE_FIELDS = [
        'addAccountDateInDate',
        'closeDateInDate',
        'fiLastUpdatedInDate',
        'lastUpdatedInDate',
    ]

    for df in DATE_FIELDS:
        if df in account:
            del account[df]
    return account

def influx_timestamp(stamp):
    date_time_obj = datetime.datetime.fromisoformat(stamp)
    return int(date_time_obj.timestamp() * 1000000000)

def networth_to_influx(timestamp, networth):
    return 'networth value=%s %d' % (networth, timestamp)

def send_networth_to_influx(timestamp, nw):
    ilp = networth_to_influx(timestamp, nw)
    print(ilp)
    send_to_influx('10.9.9.120', 'financial', ilp)

def send_to_influx(influx_host, influx_db, payload):
    url = 'http://{}:8086/write'.format(influx_host)
    querystring = {'db': influx_db}
    headers = {'cache-control': 'no-cache'}
    response = requests.request('POST', url, data=payload, headers=headers, params=querystring)
    return response.text

def accounts_to_influx_classic(timestamp, data):
    ret = []
    for a in data:
        if not a['isClosed']:
            aid = a['id'].strip()
            fiName = a['fiName'].replace(' ', '-').strip()
            name = a['cpAccountName'].replace(' ', '-').strip()
            ml4 = a['cpAccountNumberLast4'].strip()
            l4 = ml4[-4:] if ml4 else '***'
            klass = a['investmentType'].strip()
            value = a['value'].strip()

            ilp = f'balances,aid={aid},klass={klass},fi={fiName},name={name},l4={l4} value={value} {timestamp}'
            ret.append(ilp)
    return ret

def accounts_to_influx(timestamp, data: List[ModelItem]):
    ret = []
    for a in data:
        if not a.isClosed:
            aid = a.id.strip()
            fiName = a.fiName.replace(' ', '-').strip()
            name = a.cpAccountName.replace(' ', '-').strip()
            ml4 = a.cpAccountNumberLast4.strip() if a.cpAccountNumberLast4 else None
            l4 = ml4[-4:] if ml4 else '***'
            klass = a.investmentType.strip() if a.investmentType else None
            value = a.value

            ilp = f'balances,aid={aid},klass={klass},fi={fiName},name={name},l4={l4} value={value} {timestamp}'
            ret.append(ilp)
    return ret

def send_accounts_to_influx(timestamp, data):
    for payload in accounts_to_influx(timestamp, data):
        print(payload)
        send_to_influx('10.9.9.120', 'financial', payload)

def do_something():
    a = datetime.datetime.now()
    stamp = str(a)[:19]
    timestamp = influx_timestamp(stamp)

    nw, acc, inv = get_data_from_mint()

    with open("/data/networth.txt", "a") as file:
        file.write(f'{stamp} {nw:.2f}\n')

    for account in acc:
        remove_account_datetimes(account)

    acc_js = json.dumps(acc, skipkeys=True)

    with open("/data/accounts_js.txt", "a") as file:
        file.write(f'{stamp} {acc_js}\n')

    with open("/data/investments.txt", "a") as file:
        file.write(f'{stamp} {inv}\n')

    send_networth_to_influx(timestamp, nw)
    send_accounts_to_influx(timestamp, acc)

def main():
    do_something()

if __name__ == "__main__":
    main()
