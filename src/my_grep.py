class my_grep(object):

    def __init__(self, option, pattern, file):
        self.option = option.upper().split()  # option list
        self.pattern = pattern  # pattern str
        self.file = file  # file name str

    def load_data(self):
        
        pass

    def find_pattern(self):
        pass

    def print_pattern(self):
        print(self.find_pattern())
