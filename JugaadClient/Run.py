__author__ = 'Nathan'

import argparse
import sys
import configparser

from yapsy.PluginManager import PluginManagerSingleton
from yapsy.VersionedPluginManager import VersionedPluginManager

from pluginCategories.CommandIPlugin import CommandIPlugin


class Run():
    '''
    Client side starts and executes command using CommandIPlugins
    '''
    def __init__(self, parser):
        self.parser = parser
        self.pluginManager = None
        self.pluginPlaces = ["plugins"]
        self.pluginCategories = {'Command':CommandIPlugin}
        self.configFile = "Config/Client.ini"
        self.config = configparser.ConfigParser()

        self.prepPluginManager()
        self.loadPlugins()
        self.activatePlugins()
        self.callPlugin()

    def prepPluginManager(self):
        PluginManagerSingleton.setBehaviour([VersionedPluginManager,])
        self.pluginManager = PluginManagerSingleton.get()
        self.pluginManager.setPluginPlaces(self.pluginPlaces)

    def loadPlugins(self):
        self.pluginManager.setCategoriesFilter(self.pluginCategories)
        self.pluginManager.collectPlugins()

    def activatePlugins(self):
        for category in self.pluginCategories.keys():
            for plugin in self.pluginManager.getPluginsOfCategory(category):
                plugin.plugin_object.activate()

    def callPlugin(self):
        for plugin in self.pluginManager.getPluginsOfCategory('Command'):
            if (sys.argv[1] == plugin.name):
                self.executePlugin(plugin)
                return
        self.printHelp()

    def executePlugin(self, plugin):
        self.config.read(self.configFile)
        plugin.plugin_object.execute(self.config)

    def printHelp(self):
        print("Incorrect command provided. Please select from the below:")
        for category in self.pluginCategories.keys():
            for plugin in self.pluginManager.getPluginsOfCategory(category):
                print(plugin.name)
        sys.exit(0)

if __name__ == "__main__":
    Run(argparse.ArgumentParser(description="Execute jugaad client commands"))

