__author__ = 'Nathan'

from yapsy.IPlugin import IPlugin


class CommandIPlugin(IPlugin):

    def activate(self):
        super().activate()
        print(self.__class__.__name__+" is active")

    def deactivate(self):
        super().deactivate()

    def execute(self, config):
        pass

