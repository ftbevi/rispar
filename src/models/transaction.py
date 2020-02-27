class Transaction:

    def __init__(self, account_number, value):
        self.account = account_number
        self.value = value

    def __repr__(self):
        return f'transaction - accoutn {self.account}'

    @staticmethod
    def create_transaction_list(rows):
        if(len(rows) > 0):
            return [Transaction(row[0], row[1]) for row in rows]
