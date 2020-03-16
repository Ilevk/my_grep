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

    def test_find_pattern_with_option_F(self):
        '''
        Test Option F, Find Pattern as plain text
        '''
        mg = My_grep(option='F',
                     pattern='classical',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[6, 27, 36], 'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[7, 208, 217], 'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)

    def test_find_pattern_with_option_G(self):
        '''
        Test Option G, Find Pattern as Regular Expression
        '''
        mg = My_grep(option='G',
                     pattern='classi*',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[6, 27, 33], 'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[7, 208, 214], 'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)


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
