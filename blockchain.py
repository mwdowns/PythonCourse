# initialize blockchain list
blockchain = []


def get_last_blockchain_val():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def add_value(val, last_transaction=[2]):
    """
    Append a new value and previous value to blockchain.

    Arguemnts:
        val = float, new value to add to blockchain
        last_transaction = the last transaction of blockchain, default = [2]
    """
    blockchain.append([last_transaction, val])


def get_user_input():
    """ Returns a float for the user input. """
    return float(input("Your transaction amount? "))


tx_amount = get_user_input()
add_value(val=tx_amount)
tx_amount = get_user_input()
add_value(val=tx_amount, last_transaction=get_last_blockchain_val())
tx_amount = get_user_input()
add_value(val=tx_amount, last_transaction=get_last_blockchain_val())

print(blockchain)