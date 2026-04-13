from collections import OrderedDict


class Transaction:
    
    def __init__(self, transaction):
        self.sender = transaction['sender']
        self.recipient = transaction['recipient']
        self.amount = transaction['amount']

    def parse_transaction(self):
        return OrderedDict({ 'sender': self.sender, 'recipient': self.recipient, 'amount': self.amount })

    def verify_transaction(self, wallet, reward):
        balance = wallet['balance']
        if self.amount >= (balance + reward) or self.amount > reward:
            return False
        return True