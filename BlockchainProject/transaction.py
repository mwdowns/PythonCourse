from BlockchainProject.blockchain import MINING_REWARD
from BlockchainProject.wallet import wallet

participents = {'Matt'}

def add_transaction(sender, recipient, value=1.0):
    """
    Create a dict for a new transaction. If not a valid transaction, returns false.

    Arguemnts:
        sender = string, sender of transaction
        recipient = string, recipient of transactiion
        value = float, value of transaction (default = 1.0)
    """
    if verify_transaction(value):
        transaction = { 'sender': sender, 'recipient': recipient, 'value': value }
        participents.add(sender)
        participents.add(recipient)
        return transaction
    return False


def verify_transaction(value):
    """
        Verifies a transaction amount against a user's balance or the mining reward. Returns true if amount is valid.
    
        Argument:
            value = float, value of transaction
    """
    balance = wallet['balance']
    if value >= (balance + MINING_REWARD) or value > MINING_REWARD:
        return False
    return True