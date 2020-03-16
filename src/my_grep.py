import re
import logging


class My_grep(object):
    def __init__(self, option='', pattern='', file=''):
        self._context = None
        self._option = option
        self._pattern = pattern
        self._file = file

        self._isRegEx = None
        self._isIgnoreCase = False

        self._found_pattern = None
        self._isFind = False

        self.set_option()

    def load_find(self):
        self.load_data()
        self.find_pattern()

    def load_data(self):
        """
        Load Text file and Read Text data,
        Assign Texts to self.context variable
        """
        logging.info(f'Load Text File: {self._file}')

        try:
            logging.info('Open Text File')
            with open(self._file) as f:
                logging.info('Read Text File')
                self._context = f.read().split('\n')
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
        if self._option is empty, Handle pattern as Plain Text
        """
        # set option F, G
        if 'F' in self._option and 'G' in self._option:
            idx_F = self._option.index('F')
            idx_G = self._option.index('G')
        elif self._option == '' or 'F' in self._option:
            idx_F = 1
            idx_G = 0
        else:
            idx_F = 0
            idx_G = 1

        if 'i' in self._option:
            self._isIgnoreCase = True

        self._isRegEx = True if idx_G > idx_F else False

    def find_pattern(self):
        """
        Find pattern with context

        :return: Boolean, whether find or not find
        """
        find_list = list()
        self._isFind = True

        if self.isRegEx:
            logging.info('Using pattern as Regular Expression')

            if self._isIgnoreCase:
                logging.info('Ignoring Case')
                p = re.compile(self._pattern, re.I)
            else:
                p = re.compile(self._pattern)

            for i, text in enumerate(self._context):
                m = p.search('r' + text)
                if m is not None:
                    logging.info(f'{m.group()} is matched')
                    find_list.append([[i + 1, m.start() - 1, m.end() - 1], text.replace('\n', '')])
        else:
            logging.info('Using pattern as Plain Text')
            p_len = len(self._pattern)

            if self._isIgnoreCase:
                tmp_context = [c.upper() for c in self._context]
                tmp_pattern = self._pattern.upper()
            else:
                tmp_context = self._context
                tmp_pattern = self._pattern

            for i, (tmp_text, original_text) in enumerate(zip(tmp_context, self._context)):
                start_idx = tmp_text.find(tmp_pattern)
                if start_idx != -1:
                    logging.info(f'[Line {i + 1}]{self._pattern} is matched')
                    find_list.append([[i + 1, start_idx, start_idx + p_len], original_text.replace('\n', '')])

        if len(find_list) < 1:
            logging.info('No matched text is here.')
            return False

        self._found_pattern = find_list
        logging.info('Matched Text assign')
        return True

    def print_pattern(self):
        """
        Print pattern
        """
        if self._found_pattern is not None:
            for (i, text) in self._found_pattern:
                print_text = ''.join((text[:i[1]], "\033[31m", text[i[1]:i[2]], "\033[0m", text[i[2]:]))
                print(f'[Line {i[0]}]: {print_text}')
        elif self._isFind:
            logging.info('Not Found Any texts matched with pattern')
        else:
            logging.info('Please Run find pattern')

    def reset(self, option=None, pattern=None, file=None):
        """
        Reset My Grep
        :param option:  str
        :param pattern: str
        :param file:    str
        """
        logging.info('Reset My grep')

        if option is not None:
            self._option = option
            self.set_option()
            self._isRegEx = None
        if pattern is not None:
            logging.info(f'Set new Pattern: {pattern}')
            self._pattern = pattern
            logging.info('Initialize variables related to patterns')
        if file is not None:
            logging.info(f'Set new file: {pattern}')
            self._file = file
            self.load_data()

        self._found_pattern = None
        self._isFind = False

    @property
    def context(self):
        return self._context

    @property
    def option(self):
        return self._option

    @property
    def pattern(self):
        return self._pattern

    @property
    def file(self):
        return self._file

    @property
    def isRegEx(self):
        return self._isRegEx

    @property
    def found_pattern(self):
        if self._found_pattern is not None:
            return self._found_pattern
        else:
            logging.info('Please Run find pattern')
            return None
