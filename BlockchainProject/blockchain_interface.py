import hashlib

from classes.node import Node

def hash_name(name):
    return hashlib.sha256(str(name).encode()).hexdigest()

print('Hello! Welcome to MattChain!')
name = input("What's your name? ")

n = Node(hash_name(name))
n.run_node()

print('Thank you for visitng MattChain!')