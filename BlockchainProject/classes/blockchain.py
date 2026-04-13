import json

from classes.block import Block
from classes.transaction import Transaction



class Blockchain:
    MINING_REWARD = 10.0  

    def __init__(self, owner):
        self.owner = owner
        self.file_name = owner.lower() + '_blockchain.txt'
        self.blockchain, self.open_transactions = self.initialize_blockchain()

    def initialize_blockchain(self):
        try:
            self.read_chain()
        except (FileNotFoundError, IOError, IndexError):
            print('creating genesis block')
            genesis_block = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100}
            return [genesis_block], []
    
    def read_chain(self):
        with open(self.file_name, mode='r') as f:
            data = f.readlines()
            blockchain = [Block(block).parse_block() for block in json.loads(data[0][:-1])]
            open_transactions = [Transaction(tx).parse_transaction() for tx in json.loads(data[1])]
            return blockchain, open_transactions

    def save_chain(self):
        try:
            with open(self.file_name, mode='w') as f:
                f.write(json.dumps(self.blockchain))
                f.write('\n')
                f.write(json.dumps(self.open_transactions))
        except IOError:
            print('could not save file')

    def add_transaction(self, transaction):
        pass

    def mine(self):
        pass