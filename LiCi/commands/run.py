""" The run command:
    run takes a sub routine and performs its actions
"""
from .routine import Routine
from .base import Base

class Run(Base):

    def run(self):
        routine_name = self.options['<routine>']
        routine = Routine(routine_name)
        routine.details()
        print("----------Routine Started----------")
        routine.run()
        print("----------Routine Complete----------")
