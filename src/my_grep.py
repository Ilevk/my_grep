import logging


class My_grep(object):
    def __init__(self, option='', pattern='', file=''):
        self.context = ''
        self.option = option.upper().split()  # option list
        self.pattern = pattern  # pattern str
        self.file = file  # file name str

    def load_data(self):
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

    def print_pattern(self):
        print(self.find_pattern())
