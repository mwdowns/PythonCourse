import hashlib
import json
import time


class Block:
    
    def __init__(self, data):
        self.__MINING_KEY = '00'
        self.previous_hash = data['previous_hash']
        self.index = data['index']
        self.transactions = data['transactions']
        self.proof = data['proof']
        self.created_at = data['created_at'] if 'created_at' in data else time.time()

    def parse_block(self):
        return { 'previous_hash': self.previous_hash, 'index': self.index, 'transactions': self.transactions, 'proof': self.proof, 'created_at': self.created_at }

    def mine_block(self, open_transactions):
        hashed_block = self.__hash_block()
        return [hashed_block, self.__proof_of_work(hashed_block, open_transactions)]
    
    def __hash_block(self):   
        return hashlib.sha256(json.dumps(self.block, sort_keys=True).encode()).hexdigest()
    
    def __proof_of_work(self, hashed_block, open_transactions):
        proof = 0
        while not self.__valid_proof(open_transactions, hashed_block, proof):
            proof += 1
        return proof
    
    def __valid_proof(self, transactions, last_hash, proof):
        guess = (str(transactions) + str(last_hash) + str(proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[0:2] == self.__MINING_KEY