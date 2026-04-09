from BlockchainProject.transaction import add_transaction
from BlockchainProject.blockchain import owner, mine_block, verify_chain
from BlockchainProject.wallet import update_wallet, get_balance
running = True


def get_user_input():
    """ Returns a int for the user input. """
    return int(input("Your option: "))


def get_transaction_value():
    """ Returns a tuple for for transaction of recipient and value. """
    recipient = input("Who are you sending money to? ")
    tx_amount = float(input("What is the transaction amount? "))
    return recipient, tx_amount


def show_menu():
    print("Please choose option.")
    print("1. Add transaction.")
    print("2. Get balance.")
    print("3. Exit")


def exit():
    print("Goodbye!")


while running:
    show_menu()

    input_value = get_user_input()
    if input_value == 1:
        recipient, tx_amount = get_transaction_value()
        transaction = add_transaction(sender=owner, recipient=recipient, value=tx_amount)
        if transaction:
            mine_block(transaction=transaction)
            update_wallet()
        else:
            print('not enough funds')
            continue
    elif input_value == 2:
        print('Balance for {}: {:.2f}'.format(owner, get_balance(owner)))
    elif input_value == 3:
        exit()
        running = False
    else:
        print('Invalid option!')

    if not verify_chain():
        print('Invalid block in blockchain.')
        running = False