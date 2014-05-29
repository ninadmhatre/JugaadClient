__author__ = 'Nathan'

import argparse
import configparser

from pluginCategories.CommandIPlugin import CommandIPlugin


class TaskRequester(CommandIPlugin):

    def __init__(self):
        super().__init__()
        self.args = None
        self.main_server_hostname = None
        self.main_server_Port = None

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def _processArgs(self):
        parser = argparse.ArgumentParser(usage='%(prog)s TaskRequester [options]')
        parser.add_argument("TaskRequester", help="Request Jugaad main server for any tasks assigned to it.")
        #parser.add_argument("-x", "--x")
        self.args = parser.parse_args()
        print("Args:"+str(vars(self.args)))

    def _getConfig(self, config):
        if config == []:
            print("No config file found")
        else:
            self.main_server_hostname = config['JUGAAD_MAIN_HOST']['Host']
            self.main_server_port = config['JUGAAD_MAIN_HOST']['Port']
            print ("Using jugaad server at "+self.main_server_hostname+":"+self.main_server_port)

    def _contactMainServer(self):
        '''
         Contact the main server and get a reply. Call the relevant plugin depends on the response
        '''
        pass

    def execute(self, config):
        self._processArgs()
        self._getConfig(config)
        self._contactMainServer()


