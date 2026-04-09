from BlockchainProject.blockchain import blockchain, owner

def initialize_wallet(owner): 
    # wallet balance will be from blockchain
    return { 'name': owner, 'balance': get_balance(owner) }


def get_balance(participent):
    sent = sum([sum(list) for list in [[tx['value'] for tx in block['transaction'] if tx['sender'] == participent] for block in blockchain]])
    recieved = sum([sum(list) for list in [[tx['value'] for tx in block['transaction'] if tx['recipient'] == participent] for block in blockchain]])
    return recieved - sent


wallet = initialize_wallet(owner)


def update_wallet():
    wallet['balance'] = get_balance(wallet['name'])
    print(wallet['balance'])