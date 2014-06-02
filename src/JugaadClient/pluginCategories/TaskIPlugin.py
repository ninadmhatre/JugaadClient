__author__ = 'Nathan'

from yapsy.IPlugin import IPlugin


class TaskIPlugin(IPlugin):

    def activate(self):
        super().activate()
        print(self.__class__.__name__+" is active")

    def deactivate(self):
        super().deactivate()



