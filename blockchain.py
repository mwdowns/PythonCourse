# initialize blockchain list
blockchain = []


def get_last_blockchain_val():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(val, last_transaction):
    """
    Append a new value and previous value to blockchain.

    Arguemnts:
        val = float, new value to add to blockchain
        last_transaction = the last transaction of blockchain
    """
    if last_transaction == None:
        last_transaction = [0]
    blockchain.append([last_transaction, val])


def get_user_input():
    """ Returns a int for the user input. """
    return int(input("Your option: "))


def get_transaction_value():
    """ Returns a float for transaction. """
    return float(input("What is the transaction amount? "))


def print_blocks():
    for block in blockchain:
        print(block)


def show_menu():
    print("Please choose option.")
    print("1. Add transaction.")
    print("2. Print blocks.")
    print("3. Exit")


def exit():
    print("Goodbye!")


while True:
    show_menu()

    input_value = get_user_input()
    if input_value == 1:
        tx_amount = get_transaction_value()
        add_value(val=tx_amount, last_transaction=get_last_blockchain_val())
    elif input_value == 2:
        print_blocks()
    elif input_value == 3:
        exit()
        break
    else:
        print('Invalid option!')