from blockchain import Blockchain

class Wallet:

    def __init__(self, blockchain):
        self.owner = blockchain.owner
        self.blockchain = blockchain.blockchain
        self.open_transactions = blockchain.open_transactions
        self.balance = self.get_balance()

    def get_balance(self):
        # open transactions that haven't been added to blockchain
        tx_sent = sum(list for list in [tx['value'] for tx in self.open_transactions if tx['sender'] == self.owner])
        # blockchain transactions
        bl_sent = sum([sum(list) for list in [[tx['value'] for tx in block['transactions'] if tx['sender'] == self.owner] for block in self.blockchain]])
        recieved = sum([sum(list) for list in [[tx['value'] for tx in block['transactions'] if tx['recipient'] == self.owner] for block in self.blockchain]])
        return recieved - (bl_sent + tx_sent)

    def update_wallet(self, blockchain=None, open_transactions=None):
        if blockchain != None:
            self.blockchain = blockchain
        if open_transactions != None:
            self.open_transactions = open_transactions
        
        self.balance = self.get_balance()
        print('wallet updated')

    
# bc = Blockchain('Matt')

# w = Wallet(blockchain=bc)

# print(w.owner)
# print(w.balance)
# open_transactions = [{ 'sender': 'Matt', 'recipient': 'Jeri', 'value': 4.5 }]
# w.update_wallet(open_transactions=open_transactions)
# print(w.balance)