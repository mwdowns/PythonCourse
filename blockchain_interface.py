from BlockchainProject.transaction import *
from BlockchainProject.blockchain import *
running = True


def get_user_input():
    """ Returns a int for the user input. """
    return int(input("Your option: "))


def get_transaction_value():
    """ Returns a float for transaction. """
    return float(input("What is the transaction amount? "))


def show_menu():
    print("Please choose option.")
    print("1. Add transaction.")
    print("2. Print blocks.")
    print("3. Exit")


def exit():
    print("Goodbye!")


while running:
    show_menu()

    input_value = get_user_input()
    if input_value == 1:
        tx_amount = get_transaction_value()
        add_transaction(blockchain=blockchain, val=tx_amount, last_transaction=get_last_blockchain_val())
    elif input_value == 2:
        print_blocks()
    elif input_value == 3:
        exit()
        running = False
    else:
        print('Invalid option!')
    
    if not verify_chain():
        print('Invalid block in blockchain.')
        running = False