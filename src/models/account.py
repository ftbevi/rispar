import os

class Account:

    def __init__(self, number, balance):
        try:
            self.number = int(number)
            self.balance = int(balance)
        except ValueError:
            raise ValueError(f'Os valores number e balance precisam ser inteiros.')

    def __repr__(self):
        return f'account - nº {self.number}'

    def calculate_balance(self, transactions):
        for transaction in transactions:
            self.balance += transaction.value
            if self.balance < 0:
                self.negative_balance_fine()

    def negative_balance_fine(self):
        self.balance += -500

    def show_balance(self):
        print(f'{self.number},{self.balance}')

    @staticmethod
    def create_accounts_list(rows):
        if(len(rows) > 0):
            return [Account(row[0], row[1]) for row in rows]
