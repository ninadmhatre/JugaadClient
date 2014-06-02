#! /bin/bash

cd test/ServerSideStubs

echo "Start the server side stubs which mimic the master server communication"
/usr/local/bin/python3.4 test/ServerSideStubs/TaskRequesterStartAll.py

echo "Run a client test"



