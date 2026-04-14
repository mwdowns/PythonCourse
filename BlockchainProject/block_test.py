import unittest

from classes.block import Block

class TestInitialBlock(unittest.TestCase):

    def test_parse_block(self):
        data = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100, 'created_at': 1776187276.032886}
        b = Block(data=data)
        self.assertEqual(
            b.parse_block(),
            data,
            'could not parse block'
        )

    def test_mine_block(self):
        open_transactions = []
        data = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100, 'created_at': 1776187276.032886}
        b = Block(data=data)
        self.assertEqual(
            b.mine_block(open_transactions=open_transactions),
            ['12a84ebb1e50cd4606a56a45d4378c4a8573f91fb29a1bfb5daf2bd777aa0cb9', 1011],
            'could not mine block'
        )

if __name__ == '__main__':
    unittest.main()