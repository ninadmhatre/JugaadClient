__author__ = 'Nathan'

import argparse

from pluginCategories.CommandIPlugin import CommandIPlugin

class TaskRequester(CommandIPlugin):

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def processArgs(self):
        parser = argparse.ArgumentParser(usage='%(prog)s TaskRequester [options]')
        parser.add_argument("TaskRequester", help="Request Jugaad main server for any tasks assigned to it.")
        parser.add_argument("-x", "--x")
        self.args = parser.parse_args()

    def execute(self):
        self.processArgs()