from classes.blockchain import Blockchain
from classes.transaction import Transaction

class Node:
    
    def __init__(self):
        self.running = True

    def run_node(self):
        bc = Blockchain('Matt')
        w = bc.wallet
        while self.running:
            self.show_menu()

            input_value = self.get_user_input()
            if input_value == 1:
                bc.mine()
            elif input_value == 2:
                recipient, tx_amount = self.get_transaction_value()
                transaction = Transaction({'sender': bc.owner, 'recipient': recipient, 'amount': tx_amount})
                if bc.add_transaction(transaction=transaction):
                    w.update_wallet()
                else:
                    print('not enough funds')
                    continue
            elif input_value == 3:
                print('Balance for {}: {:.2f}'.format(bc.owner, w.get_balance()))
            elif input_value == 4:
                self.exit()
                self.running = False
            else:
                print('Invalid option!')

            if not bc.verify_chain():
                self.running = False
    
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
        print("1. Mine block.")
        print("2. Add transaction.")
        print("3. Get balance.")
        print("4. Exit")


    def exit():
        print("Goodbye!")