__author__ = 'Nathan'

import configparser
import os
import re
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class TaskRequester_Grid(threading.Thread):

    def __init__(self):
        self.config_file = "Testing.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self.port = int(self.config[self.__class__.__name__]['Port'])
        threading.Thread.__init__(self)
        self.stop = threading.Event()

    def run(self):
        print("Starting server from :"+os.getcwd())
        httpd = HTTPServer(('', self.port), myHandler)
        while not self.stop.is_set():
            httpd.handle_request()

    def stopit(self):
        self.stop.set()

from urllib.parse import urlparse, parse_qs

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self._parseURL()
        print( "Command: %s Path: %s Headers: %r"
            % ( self.command, self.path, self.headers.items() ) )
        self._writeResponseAndHeaders()
        self._encodeThenWriteData("GRID")

    def _parseURL(self):
        params = urlparse(self.path)
        self.urlPath = params[2]
        self.urlParams = parse_qs(params[4], True)
        print(self.urlPath)
        print(self.urlParams)

    def _writeResponseAndHeaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def _encodeThenWriteData(self, d):
        self.wfile.write(bytes(d, 'UTF-8'))

if __name__ == "__main__":
    TaskRequester_Grid().start()