import unittest
import os

from src.models.account import Account
from src.models.file import File
from src.models.transaction import Transaction

CSV_FOLDER = os.path.join(os.path.dirname(__file__), 'csv')

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transactions = [Transaction(
            345, -1000), Transaction(345, 1500), Transaction(347, -2500)]
        self.accounts = [Account(345, 14428), Account(347, 15000)]

    def test_init_transaction_error(self):
        with self.assertRaises(ValueError):
            Transaction('345', '')

    def test_create_transaction_list(self):
        rows = File.read_csv(f'{CSV_FOLDER}/transactions.csv')
        transactions = Transaction.create_transaction_list(rows)
        self.assertEqual(len(transactions), 4)

    def test_create_transaction(self):
        account = Account(345, 14428)
        transactions = Transaction.find_transaction(self.transactions, account)
        self.assertEqual(len(transactions), 2)
