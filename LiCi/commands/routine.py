import os
import yaml

from subprocess import call
from .options.remote import Remote

class Routine(object):

    def __init__(self, routine_yaml):
        current_dir = os.path.dirname(__file__)
        rel_path = "../routines/{}.yaml".format(routine_yaml)
        file_path = os.path.join(current_dir,rel_path)
        with open(file_path, 'r') as stream:
            try:
                routine = dict(yaml.load(stream))
            except yaml.YAMLError as exc:
                print(exc)
        self.name = routine['name']
        self.repo = routine['repo']
        self.build_commands = routine['build_commands']

    def details(self):
        print("Routine: ", self.name)
        print("Build Commands: ", self.build_commands)

    def run(self):
        src_info = Remote(self.repo)
        commands = self.build_commands.split(" ")
        call(commands)
