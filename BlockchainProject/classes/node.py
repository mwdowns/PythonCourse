from classes.blockchain import Blockchain
from classes.transaction import Transaction

class Node:
    
    def __init__(self, wallet_id):
        self.running = True
        self.wallet_id = wallet_id

    def run_node(self):
        bc = Blockchain(self.wallet_id)
        w = bc.wallet
        while self.running:
            self.__show_menu()

            input_value = self.__get_user_input()
            if input_value == 1:
                bc.mine()
            elif input_value == 2:
                recipient, tx_amount = self.__get_transaction_value()
                transaction = Transaction({'sender': bc.owner, 'recipient': recipient, 'amount': tx_amount})
                if bc.add_transaction(transaction=transaction):
                    w.update_wallet()
                else:
                    print('not enough funds')
                    continue
            elif input_value == 3:
                print('Balance for {}: {:.2f}'.format(bc.owner, w.get_balance()))
            elif input_value == 4:
                self.__exit()
                self.running = False
            else:
                print('Invalid option!')

            if not bc.verify_chain():
                self.running = False
    
    def __get_user_input(self):
        """ Returns a int for the user input. """
        return int(input("Your option: "))


    def __get_transaction_value(self):
        """ Returns a tuple for for transaction of recipient and value. """
        recipient = input("Who are you sending money to? ")
        tx_amount = float(input("What is the transaction amount? "))
        return recipient, tx_amount


    def __show_menu(self):
        print("Please choose option.")
        print("1. Mine block.")
        print("2. Add transaction.")
        print("3. Get balance.")
        print("4. Exit")


    def __exit(self):
        print("Goodbye!")