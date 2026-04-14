import json

from classes.block import Block
from classes.transaction import Transaction
from classes.wallet import Wallet
from classes.participants import Participants


class Blockchain:
    __MINING_REWARD = 10.0  

    def __init__(self, owner):
        self.owner = owner
        self.file_name = 'mattchain.txt'
        self.blockchain, self.open_transactions = self.initialize_blockchain()
        self.wallet = Wallet(blockchain=self)
        self.participants = Participants()

    def initialize_blockchain(self):
        try:
            self.read_chain()
        except (FileNotFoundError, IOError, IndexError):
            print('creating genesis block')
            genesis_block = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100, 'created_at': 1776187276.032886}
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
        """
        Add verified transaction dict to open_transactions list

        Arguemnts:
            transaction = Transaction object, takes the verifity_transaction method which returns true or false
            wallet = Wallet object, used in verify_transaction to check balance
            participants = Participants object, keeps track of participants
        """
        result = transaction.verify_transaction(self.wallet.balance, self.__MINING_REWARD)
        print('----')
        print(result)
        print('----')
        if result:
            self.open_transactions.append(transaction.parse_transaction())
            self.participants.add_participant(transaction.sender)
            self.participants.add_participant(transaction.recipient)
            self.save_chain()
        return result

    def mine(self, wallet):
        last_block = Block(self.blockchain[-1])
        hashed_block, proof = last_block.mine_block()
        reward_transaction = Transaction({'sender': 'MINING', 'recipient': wallet.owner, 'value': self.__MINING_REWARD}).parse_transaction()
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = {'previous_hash': hashed_block, 'index': len(self.blockchain), 'transactions': copied_transactions, 'proof': proof}
        self.blockchain.append(block)
        self.open_transactions.clear()
        self.save_chain()

    # not sure this will work
    def verify_chain(self):
        """ Verifies the blocks of the blockchaing and returns False if any block is invalid. """
        for index, block in enumerate(self.blockchain):
            if index == 0:
                continue
            last_block_mined = Block(self.blockchain[index - 1]).mine_block(self.open_transactions)
            if block['previous_hash'] != last_block_mined[0]:
                print('Invalid hash')
                return False
            proof_check = Block({
                'index': block['index'],
                'last_hash': block['last_hash'],
                'transactions': block['transactions'][:-1],
                'proof': block['proof']
                }).mine_block(self.open_transactions)
            if block['proof'] != proof_check[1]:
                print('Proof of Work invalid')
                return False
        return True