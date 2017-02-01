""" The run command:
    run takes a sub routine and performs its actions
"""

from .base import Base

class Run(Base):

    def run(self):
        print("running routine {X}")
