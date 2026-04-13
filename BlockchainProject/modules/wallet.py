from modules.blockchain import owner, open_transactions, blockchain

def initialize_wallet(owner):
    # wallet balance will be from blockchain
    return { 'name': owner, 'balance': get_balance(owner) }

# add to wallet class DONE
def get_balance(participent):
    # open transactions that haven't been added to blockchain
    tx_sent = sum(list for list in [tx['value'] for tx in open_transactions if tx['sender'] == participent])
    # blockchain transactions
    bl_sent = sum([sum(list) for list in [[tx['value'] for tx in block['transactions'] if tx['sender'] == participent] for block in blockchain]])
    recieved = sum([sum(list) for list in [[tx['value'] for tx in block['transactions'] if tx['recipient'] == participent] for block in blockchain]])
    return recieved - (bl_sent + tx_sent)


wallet = initialize_wallet(owner)

# add to wallet class DONE
def update_wallet():
    wallet['balance'] = get_balance(wallet['name'])
    print(wallet['balance'])