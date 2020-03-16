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
            logging.warning(f'Raise {Error}')
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

        def find_pattern_next(sub_i, sub_p, sub_text, matched_list, offset) :
            """
            Find pattern with subtext recursively
            """
            m = sub_p.search(sub_text)
            if m is not None:
                matched_list.append([sub_i + 1, offset + m.start(), offset + m.end()])

                if len(sub_text[m.end() - 1:]) > len(self._pattern):
                    find_pattern_next(sub_i, sub_p, sub_text[m.end() - 1:], matched_list, offset + m.end() - 1)

        find_list = list()
        self._isFind = True

        if self.isRegEx:
            logging.info('Using Pattern as Regular Expression')
            print('Using Pattern as Regular Expression')
            tmp_pattern = fr"{self._pattern}"
        else:
            tmp_pattern = re.escape(fr"{self._pattern}")

        if self._isIgnoreCase:
            logging.info('Ignoring Case')
            print('Ignoring Case')
            p = re.compile(tmp_pattern, re.I)
        else:
            p = re.compile(tmp_pattern)

        for i, text in enumerate(self._context):
            tmp_list = list()
            find_pattern_next(i, p, text, tmp_list, 0)
            if len(tmp_list) > 0 :
                find_list.append([tmp_list, text.replace('\n', '')])

        if len(find_list) < 1:
            logging.warning('No matched Text is here.')
            return False

        self._found_pattern = find_list
        logging.info('Matched Text assign')
        return True

    def print_pattern(self):
        """
        Print pattern
        """
        if self._found_pattern is not None:
            for (idxes, text) in self._found_pattern:
                result = ''
                prev_idx = 0
                for idx in idxes :
                    result += ''.join((text[prev_idx:idx[1]], "\033[31m", text[idx[1]:idx[2]], "\033[0m"))
                    prev_idx = idx[2]
                result += text[prev_idx:]
                print(f'[Line {idx[0]}]: {result}')
        elif self._isFind:
            logging.warning('Not Found any texts matched with pattern')
        else:
            logging.warning('Please Run find pattern')

    def reset(self, option=None, pattern=None, file=None):
        """
        Reset My Grep
        :param option:  str
        :param pattern: str
        :param file:    str
        """
        logging.info('Reset My grep')
        print('Reset My grep')

        if option is not None:
            self._option = option
            self.set_option()
            self._isRegEx = None
        if pattern is not None:
            logging.warning(f'Set new Pattern: {pattern}')
            self._pattern = pattern
            logging.warning('Initialize variables related to patterns')
        if file is not None:
            logging.warning(f'Set new file: {pattern}')
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
            logging.warning('Please Run find pattern')
            return None
