__author__ = 'Nathan'

import argparse

from pluginCategories.CommandIPlugin import CommandIPlugin

class RegisterRepo(CommandIPlugin):

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def processArgs(self):
        parser = argparse.ArgumentParser(usage='%(prog)s RegisterRepo [options]')
        parser.add_argument("RegisterRepo", help="Registers this repo with main server")
        parser.add_argument("-y", "--y")
        self.args = parser.parse_args()

    def execute(self, x):
        self.processArgs()