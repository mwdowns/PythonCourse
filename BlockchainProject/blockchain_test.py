import os
import unittest

from classes.blockchain import Blockchain
from classes.transaction import Transaction

class TestInitialBlockchain(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove('mattchain.txt')
        except FileNotFoundError:
            pass
    
    def test_file_name(self):
        owner = 'some-hash'
        bc = Blockchain(owner)
        self.assertEqual(
            bc.file_name,
            'mattchain.txt',
            'the file name is wrong'
        )
    
    def test_first_run_blockchain(self):
        owner = 'some-hash'
        bc = Blockchain(owner)
        self.assertEqual(
            bc.blockchain,
            [{'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100, 'created_at': 1776187276.032886}],
            'blockchain not initialized with genesis block'
        )

    def test_first_run_open_transactions(self):
        owner = 'some-hash'
        bc = Blockchain(owner)
        self.assertEqual(
            bc.open_transactions,
            [],
            'open transactions not initialized'
        )
    
    def test_wallet(self):
        owner = 'some-hash'
        bc = Blockchain(owner)
        self.assertEqual(
            bc.wallet.balance,
            0,
            'wallet balance is not 0'
        )

    def test_particpants(self):
        owner = 'some-hash'
        bc = Blockchain(owner)
        self.assertEqual(
            len(bc.participants.participants),
            0,
            'participents is not empty'
        )

    def test_add_transaction(self):
        owner = 'some-hash'
        too_big_tx = Transaction({ 'sender': owner, 'recipient': 'some-other-hash', 'amount': 11.0 })
        ok_tx = Transaction({ 'sender': owner, 'recipient': 'some-other-hash', 'amount': 9.0 })
        bc = Blockchain(owner)
        self.assertFalse(bc.add_transaction(too_big_tx))
        self.assertTrue(bc.add_transaction(ok_tx))

if __name__ == '__main__':
    unittest.main()