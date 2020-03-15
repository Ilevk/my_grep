import re
import logging


class My_grep(object):
    def __init__(self, option='', pattern='', file=''):
        self.context = None
        self.option = option # option list
        self.pattern = pattern  # pattern str
        self.file = file  # file name str

        self.isRegEx = None
        self.found_pattern = None

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
                self.context = f.read().split('\n')
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
        find_list = list()

        if self.isRegEx:
            p = re.compile(self.pattern)
            for i, text in enumerate(self.context):
                m = p.search('r'+text)
                if m is not None:
                    print(f'{m.group()} is matched')
                    find_list.append([[i+1, m.start(), m.end()], text.replace('\n', '')])
            pass
        else:
            p_len = len(self.pattern)
            for i, text in enumerate(self.context):
                start_idx = text.find(self.pattern)
                if start_idx != -1:
                    print(f'{self.pattern} is matched')
                    find_list.append([[i+1, start_idx, start_idx+p_len], text.replace('\n', '')])

        if len(find_list) < 1:
            return False

        self.found_pattern = find_list
        return True

    def print_pattern(self):
        pass