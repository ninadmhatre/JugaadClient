__author__ = 'Nathan'

import argparse
import sys
import configparser

from yapsy.PluginManager import PluginManagerSingleton
from yapsy.VersionedPluginManager import VersionedPluginManager

# This needs to be dynamic also. Use the __init__.py??
from pluginCategories.CommandIPlugin import CommandIPlugin
from pluginCategories.TaskIPlugin import TaskIPlugin


class Chalo():
    """
    Client side starts and executes command using CommandIPlugins
    """
    def __init__(self):
        self.plugin_manager = None

        #These need to be dynamic
        self.plugin_places = ["plugins/CommandPlugins", "plugins/TaskPlugins"]
        self.plugin_categories = {'Command': CommandIPlugin, 'Task': TaskIPlugin}

        #Needs to be dynamic here!
        self.config_file = "../../ClientTesting/Config/Client.ini"
        self.config = configparser.ConfigParser()

        self.prepPluginManager()
        self.loadPlugins()
        self.activatePlugins()
        self.callPlugin()

    def prepPluginManager(self):
        PluginManagerSingleton.setBehaviour([VersionedPluginManager, ])
        self.plugin_manager = PluginManagerSingleton.get()
        self.plugin_manager.setPluginPlaces(self.plugin_places)

    def loadPlugins(self):
        self.plugin_manager.setCategoriesFilter(self.plugin_categories)
        self.plugin_manager.collectPlugins()

    def activatePlugins(self):
        for category in self.plugin_categories.keys():
            print(category+":")
            for plugin in self.plugin_manager.getPluginsOfCategory(category):
                plugin.plugin_object.activate()

    def callPlugin(self):
        for plugin in self.plugin_manager.getPluginsOfCategory('Command'):
            if len(sys.argv) > 1 and sys.argv[1] == plugin.name:
                self.executePlugin(plugin)
                return
        self.printHelp()

    def executePlugin(self, plugin):
        self.config.read(self.config_file)
        plugin.plugin_object.execute(self.config)

    def printHelp(self):
        print("Incorrect command provided. Please select from the below:")
        for plugin in self.plugin_manager.getPluginsOfCategory('Command'):
            print("    "+plugin.name)
        sys.exit(0)

if __name__ == "__main__":
    Chalo()

