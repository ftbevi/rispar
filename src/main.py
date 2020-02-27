import sys

from models.file import File
from models.account import Account
from models.transaction import Transaction

if __name__ == "__main__":
    if len(sys.argv) > 1:
        account_file_path = sys.argv[1]
        transactions_file_path = sys.argv[2]
        # Get accounts rows.
        account_rows = File.read_csv(account_file_path)
        accounts = Account.create_accounts_list(account_rows)
        # Get transactions rows.
        transaction_rows = File.read_csv(transactions_file_path)
        transactions = Transaction.create_transaction_list(transaction_rows)
