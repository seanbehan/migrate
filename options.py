import sys

class Options(object):
    def __init__(self):
        self.options = {}
    def add(self, flag, callback):
        self.options[flag] = callback
    def execute(self):
        if len(sys.argv) > 2:
            self.options[sys.argv[1]](sys.argv[2])
        else:
            self.options[sys.argv[1]]()
