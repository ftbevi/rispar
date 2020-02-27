class Account:

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def __repr__(self):
        return f'account - nº {self.number}'

    @staticmethod
    def create_accounts_list(rows):
        if(len(rows) > 0):
            return [Account(row[0], row[1]) for row in rows]
