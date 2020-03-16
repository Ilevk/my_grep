import os
from os.path import join

import unittest
from src.my_grep import *


class TestOptions(unittest.TestCase):
    def test_set_option_FG(self):
        """
        Test Setting Option FG Priority
        """
        mg = My_grep(option='FG',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, True)

    def test_set_option_GF(self):
        """
        Test Setting Option GF Priority
        """
        mg = My_grep(option='GF',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, False)

    def test_set_option_G(self):
        """
        Test Setting Option F
        """
        mg = My_grep(option='G',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, True)

    def test_set_option_F(self):
        """
        Test Setting Option F
        """
        mg = My_grep(option='F',
                     pattern='test_pattern',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        self.assertEqual(mg.isRegEx, False)

    def test_find_pattern_with_option_F(self):
        """
        Test Option F, Find Pattern as plain text
        """
        mg = My_grep(option='F',
                     pattern='classical',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[6, 27, 36]], 'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[[7, 208, 217]], 'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)

    def test_find_pattern_with_option_G(self):
        """
        Test Option G, Find Pattern as Regular Expression
        """
        mg = My_grep(option='G',
                     pattern='classi*',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[6, 27, 33]], 'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[[7, 208, 214]], 'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)

    def test_ignore_case_with_option_F(self):
        """
        Test Pattern with Ignore Case and Option F
        """
        mg = My_grep(option='iF',
                     pattern='classical',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[6, 27, 36]],
                               'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[[7, 208, 217]],
                               'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)

    def test_ignore_case_with_option_G(self):
        """
        Test Pattern with Ignore Case and Option G
        """
        mg = My_grep(option='iG',
                     pattern='classi*',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[6, 27, 33]], 'It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'],
                              [[[7, 208, 214]], 'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.']]
                             , mg._found_pattern)

    def test_multiple_matched_text_with_option_G(self):
        """
        Test Pattern with Ignore Case and Option G
        """
        mg = My_grep(option='G',
                     pattern='the*',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[1, 36, 39]],
                               'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'],
                              [[[2, 21, 24],
                                [2, 67, 70]],
                               "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."],
                              [[[3, 50, 53]],
                               'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'],
                              [[[4, 22, 25],
                                [4, 34, 36],
                                [4, 37, 40],
                                [4, 121, 123]],
                               'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'],
                              [[[7, 94, 97],
                                [7, 175, 177],
                                [7, 183, 186],
                                [7, 196, 199],
                                [7, 241, 244]],
                               'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'],
                              [[[9, 27, 30],
                                [9, 31, 34],
                                [9, 42, 44],
                                [9, 69, 72]],
                               'This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.']]
                             , mg._found_pattern)

    def test_multiple_matched_text_with_option_F(self):
        """
        Test Pattern with Ignore Case and Option F
        """
        mg = My_grep(option='F',
                     pattern='the',
                     file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertTrue(mg.find_pattern())
        self.assertListEqual([[[[1, 36, 39]],
                               'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'],
                              [[[2, 21, 24],
                                [2, 67, 70]],
                               "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."],
                              [[[3, 50, 53]],
                               'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'],
                              [[[4, 22, 25],
                                [4, 37, 40]],
                               'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'],
                              [[[7, 94, 97],
                                [7, 183, 186],
                                [7, 196, 199],
                                [7, 241, 244]],
                               'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'],
                              [[[9, 27, 30],
                                [9, 31, 34],
                                [9, 69, 72]],
                               'This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.']]
                             , mg._found_pattern)

    def test_ignore_case_with_multiple_matched_text_ption_G(self):
            """
            Test Pattern with Ignore Case and Option G
            """
            mg = My_grep(option='iG',
                         pattern='the*',
                         file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
            mg.load_data()
            self.assertTrue(mg.find_pattern())
            self.assertListEqual([[[[1, 36, 39]],
                                   'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'],
                                  [[[2, 21, 24],
                                    [2, 67, 70]],
                                   "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."],
                                  [[[3, 50, 53]],
                                   'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'],
                                  [[[4, 22, 25],
                                    [4, 34, 36],
                                    [4, 37, 40],
                                    [4, 121, 123]],
                                   'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'],
                                  [[[7, 94, 97],
                                    [7, 175, 177],
                                    [7, 183, 186],
                                    [7, 196, 199],
                                    [7, 241, 244]],
                                   'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'],
                                  [[[8, 88, 91]], 'Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.'],
                                  [[[9, 0,  2],
                                    [9, 27, 30],
                                    [9, 31, 34],
                                    [9, 42, 44],
                                    [9, 69, 72],
                                    [9, 86, 89]],
                                   'This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.']]
                                 , mg._found_pattern)

    def test_ignore_case_with_multiple_matched_text_option_F(self):
            """
            Test Pattern with Ignore Case and Option F
            """
            mg = My_grep(option='iF',
                         pattern='the',
                         file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
            mg.load_data()
            self.assertTrue(mg.find_pattern())
            self.assertListEqual([[[[1, 36, 39]],
                                   'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'],
                                  [[[2, 21, 24],
                                    [2, 67, 70]],
                                   "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."],
                                  [[[3, 50, 53]],
                                   'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'],
                                  [[[4, 22, 25],
                                    [4, 37, 40]],
                                   'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'],
                                  [[[7, 94, 97],
                                    [7, 183, 186],
                                    [7, 196, 199],
                                    [7, 241, 244]],
                                   'Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'],
                                  [[[8, 88, 91]],
                                   'Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.'],
                                  [[[9, 27, 30],
                                    [9, 31, 34],
                                    [9, 69, 72],
                                    [9, 86, 89]],
                                   'This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.']]
                                 , mg._found_pattern)

class TestLoadData(unittest.TestCase):
    def testInvalidFile(self):
        """
        Test Invalid File path
        """
        mg = My_grep(file=join(join(os.getcwd(), join('..', 'data'), 'Invalid.txt')))
        self.assertRaises(FileNotFoundError, mg.load_data)

    def testValidFile(self):
        """
        Test Valid File path
        """
        mg = My_grep(file=join(join(os.getcwd(), join('..', 'data'), 'Lorem_Ipsum.txt')))
        mg.load_data()
        self.assertIsNotNone(mg.context)


if __name__ == '__main__':
    unittest.main()
