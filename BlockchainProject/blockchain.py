MINING_REWARD = 10.0
owner = 'Matt'


def initialize_blockchain():
    # initialize blockchain list, get from file, otherwise use genesis block
    genesis_block = {'previous_hash': '', 'index': 0, 'transaction': []}
    return [genesis_block]


blockchain = initialize_blockchain()


def mine_block(transaction):
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = { 'sender': 'MINING', 'recipient': owner, 'value': MINING_REWARD }
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transaction': [reward_transaction, transaction]}
    blockchain.append(block)


def print_blocks():
    """ Prints the blocks of the blockchain. """
    for block in blockchain:
        print(block)


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def verify_chain():
    """ Verifies the blocks of the blockchaing and returns False if any block is invalid. """
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True