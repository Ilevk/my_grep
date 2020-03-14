import os
from os.path import join

import unittest
from src.my_grep import *


class TestOptions(unittest.TestCase):
    def test_option_F(self):
        pass

    def test_option_G(self):
        pass


class TestLoadData(unittest.TestCase):
    def testInvalidFile(self):
        mg = My_grep(file=join(join(os.getcwd(), join('..', 'data'), 'Invalid.txt')))
        self.assertRaises(FileNotFoundError, mg.load_data)


if __name__ == '__main__':
    unittest.main()
