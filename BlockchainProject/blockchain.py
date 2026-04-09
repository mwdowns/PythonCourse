import hashlib
import json
MINING_REWARD = 10.0
owner = 'Matt'
open_transactions = []

def initialize_blockchain():
    # initialize blockchain list, get from file, otherwise use genesis block
    genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
    return [genesis_block]


blockchain = initialize_blockchain()


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = { 'sender': 'MINING', 'recipient': owner, 'value': MINING_REWARD }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transactions': copied_transactions}
    blockchain.append(block)
    open_transactions.clear()


# def valid_proof(transaction, last_hash, proof):
#     guess = (str(transaction) + str(last_hash) + str(proof)).encode()
#     guess_hash = hashlib.sha256(guess)
#     return guess_hash[0:3] == '00'


# def proof_of_work():
#     last_block = blockchain[-1]
#     lash_hash = hash_block(last_block)
#     proof = 0
#     while valid_proof()


def print_blocks():
    """ Prints the blocks of the blockchain. """
    for block in blockchain:
        print(block)


def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()


def verify_chain():
    """ Verifies the blocks of the blockchaing and returns False if any block is invalid. """
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True