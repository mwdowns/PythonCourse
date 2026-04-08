def mine_block():
    pass

def add_transaction(blockchain, val, last_transaction):
    """
    Append a new value and previous value to blockchain.

    Arguemnts:
        val = float, new value to add to blockchain
        last_transaction = the last transaction of blockchain
    """
    if last_transaction == None:
        last_transaction = [0]
    blockchain.append([last_transaction, val])