import unittest

from src.models.account import Account
from src.models.file import File
from src.models.transaction import Transaction


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.transactions = [Transaction(345, -1000), Transaction(345, 1500)]
        self.account = Account(345, 14428)

    def test_init_error_number_value_empty(self):
        with self.assertRaises(ValueError):
            Account('', '14428')

    def test_init_error_balance_value_empty(self):
        with self.assertRaises(ValueError):
            Account('345', '')

    def test_calculate_balance(self):
        self.account.calculate_balance(self.transactions)
        self.assertEqual(self.account.balance, 14928)

    def test_calculate_balance_negative_balance(self):
        transactions = [Transaction(345, -1000), Transaction(345, -1600)]
        account = Account(345, 2500)
        account.calculate_balance(transactions)
        self.assertEqual(account.balance, -600)

    def test_create_accounts_list(self):
        rows = File.read_csv(
            'C:\\Users\\DataInfo\\Documents\\projetos\\Rispar\\rispar\\tests\\csv\\accounts.csv')
        accounts = Account.create_accounts_list(rows)
        self.assertEqual(len(accounts), 2)
