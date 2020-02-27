import sys

from models.file import File
from models.account import Account

if __name__ == "__main__":
    if len(sys.argv) > 1:
        account_file_path = sys.argv[1]
        transactions_file_path = sys.argv[2]
        # Get accounts rows.
        account_rows = File.read_csv(account_file_path)
        accounts = Account.create_accounts_list(account_rows)
        print('accounts', accounts)
        # Get transactions rows.
        # transactio_rows = File.read_csv(transactions_file_path)
        # print(transactio_rows)
