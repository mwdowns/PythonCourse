import hashlib
import json
from collections import OrderedDict
MINING_REWARD = 10.0
owner = 'Matt'
open_transactions = []

def initialize_blockchain():
    # initialize blockchain list, get from file, otherwise use genesis block
    genesis_block = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100}
    return [genesis_block]


blockchain = initialize_blockchain()


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = OrderedDict([('sender','MINING'), ('recipient', owner), ('value', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transactions': copied_transactions, 'proof': proof}
    blockchain.append(block)
    open_transactions.clear()


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof

def print_blocks():
    """ Prints the blocks of the blockchain. """
    for block in blockchain:
        print(block)


def hash_block(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


def verify_chain():
    """ Verifies the blocks of the blockchaing and returns False if any block is invalid. """
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            print('Invalid hash')
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of Work invalid')
            return False
    return True