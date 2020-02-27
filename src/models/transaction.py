class Transaction:

    def __init__(self, account_number, value):
        try:
            self.account = int(account_number)
            self.value = int(value)
        except ValueError:
            raise ValueError(f'Os valores account_number e balance precisam ser inteiros.')

    def __repr__(self):
        return f'transaction - account {self.account}'

    @staticmethod
    def create_transaction_list(rows):
        if(len(rows) > 0):
            return [Transaction(row[0], row[1]) for row in rows]

    @staticmethod
    def find_transaction(transactions, account):
        return [transaction for transaction in transactions if transaction.account == account.number]
