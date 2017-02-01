"""
lici

Usage:
    lici run
    lici -h | --help
    lici -v | --version

Options:
    -h --help   Shows this screen.
    --version   Shows the current installed version.

Examples:
    lici run 

Help:
    For help using this tool, please join the irc on freenode #LiCi or 
    open an issue on github

"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """CLI entrypoint"""
    import LiCi.commands
    options = docopt(__doc__, version=VERSION)
    
    # this loop matches the commands being run to the options provided by 
    # docopts
    for k, v in options.iteritems():
        if hassattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
