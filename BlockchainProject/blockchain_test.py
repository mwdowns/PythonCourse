import unittest

from classes.blockchain import Blockchain

class TestInitialBlockchain(unittest.TestCase):
    
    def test_file_name(self):
        name = 'Matt'
        bc = Blockchain(name)
        self.assertEqual(
            bc.file_name,
            name.lower() + '_blockchain.txt',
            'the file name is wrong'
        )
    
    def test_first_run_blockchain(self):
        bc = Blockchain('Matt')
        self.assertEqual(
            bc.blockchain,
            [{'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100}],
            'blockchain not initialized with genesis block'
        )

    def test_first_run_open_transactions(self):
        bc = Blockchain('Matt')
        self.assertEqual(
            bc.open_transactions,
            [],
            'open transactions not initialized'
        )

if __name__ == '__main__':
    unittest.main()