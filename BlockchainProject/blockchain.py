# initialize blockchain list
blockchain = []

def get_last_blockchain_val():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def print_blocks():
    for block in blockchain:
        print(block)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        block = blockchain[block_index]
        if block_index == 0:
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid