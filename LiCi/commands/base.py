""" The base command class passes in all of the docopt options that were 
    generated 
"""

class Base(object):

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError("You must implement the run() method")

