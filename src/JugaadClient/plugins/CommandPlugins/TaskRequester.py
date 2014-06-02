__author__ = 'Nathan'

import sys
import argparse
import requests

from pluginCategories.CommandIPlugin import CommandIPlugin


class TaskRequester(CommandIPlugin):

    def __init__(self):
        super().__init__()
        self.args = None
        self.main_server_hostname = None
        self.main_server_port = None
        self.contact_string = 'taskrequest'
        self.retry = 3
        self.response = None

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def _processArgs(self):
        parser = argparse.ArgumentParser(usage='%(prog)s TaskRequester [options]')
        parser.add_argument('TaskRequester', help='Request Jugaad main server for any tasks assigned to it.')
        #parser.add_argument("-x", "--x")
        self.args = parser.parse_args()
        print("Args:"+str(vars(self.args)))

    def _getConfig(self, config):
        if not config:
            print("No config file found!")
        else:
            self.main_server_hostname = config[self.__class__.__name__]['Host'] or config[DEFAULT]['Host']
            self.main_server_port = config[self.__class__.__name__]['Port'] or config[DEFAULT]['Port']
            print('Using jugaad server at '+self.main_server_hostname+':'+self.main_server_port)

    def _contactMainServerWithRetriesAndCallPlugin(self):
        for num in range(self.retry):
            if self._contactMainServer():
                self._callActionPlugin()
                break
            elif num == self.retry-1:
                print('Unable to contact master server after '+str(self.retry)+' tries. Exiting..')
                sys.exit(1)
            else:
                print('Retry '+str(num+1))

    def _contactMainServer(self):
        try:
            print('URL request:' + self._constructURL())
            self.response = requests.get(self._constructURL(), stream=True)
            print(self.response.text)
            return True
        except requests.ConnectionError:
            print("Problem connecting to master server")
        except requests.RequestException:
            print('Problem encountered sending request to master server')

    def _constructURL(self):
        return "http://"+self.main_server_hostname+":"+self.main_server_port+"/"+self.contact_string

    def _callActionPlugin(self):
        pass

    def execute(self, config):
        self._processArgs()
        self._getConfig(config)
        self._contactMainServerWithRetriesAndCallPlugin()

