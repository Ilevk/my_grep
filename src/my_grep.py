import re
import logging


class My_grep(object):
    def __init__(self, option='', pattern='', file=''):
        self.context = ''
        self.option = option # option list
        self.pattern = pattern  # pattern str
        self.file = file  # file name str
        self.isRegEx = None

        self.set_option()

    def load_data(self):
        """
        Load Text file and Read Text data,
        Assign Texts to self.context variable
        """
        logging.info(f'Load Text File: {self.file}')

        try:
            logging.info('Open Text File')
            with open(self.file) as f:
                logging.info('Read Text File')
                self.context = f.read()
                logging.info('Success Read Text File')

        except FileNotFoundError as Error:
            logging.info(f'Raise {Error}')
            raise FileNotFoundError

    def set_option(self):
        """
        Option,
        F: Handle pattern as Plain Text
        G: Handle pattern as Basic RegEx

        Behind option has a priority
        """
        # set option F, G
        if 'F' in self.option and 'G' in self.option :
            idx_F = self.option.index('F')
            idx_G = self.option.index('G')
        elif 'F' in self.option:
            idx_F = 1
            idx_G = 0
        else:
            idx_F = 0
            idx_G = 1

        self.isRegEx = True if idx_G > idx_F else False

    def find_pattern(self):
        pass

    def print_pattern(self):
        print(self.find_pattern())
