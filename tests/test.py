import os
from os.path import join

import unittest
from src.my_grep import *


class TestOptions(unittest.TestCase):
    def test_set_option_FG(self):
        mg = My_grep(option='FG',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, True)

    def test_set_option_GF(self):
        mg = My_grep(option='GF',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, False)

    def test_set_option_G(self):
        mg = My_grep(option='G',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, True)

    def test_set_option_F(self):
        mg = My_grep(option='F',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, False)

    def test_option_F(self):
        pass

    def test_option_G(self):
        pass


class TestLoadData(unittest.TestCase):
    def testInvalidFile(self):
        mg = My_grep(file=join(join(os.getcwd(), join('..', 'data'), 'Invalid.txt')))
        self.assertRaises(FileNotFoundError, mg.load_data)

    def testValidFile(self):
        mg = My_grep(file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertIsNotNone(mg.context)


if __name__ == '__main__':
    unittest.main()
