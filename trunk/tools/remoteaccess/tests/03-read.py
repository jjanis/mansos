#!/usr/bin/env python

# Get data

import os, sys, time
import urllib2

def main():
    host = "http://localhost:30001/read?port=/dev/ttyUSB0"
#    host = "http://10.0.0.1:30001/read?port=/dev/ttyUSB0"
    try:
        req = urllib2.urlopen(host)
        print("Reply data:")
        print(req.read())
    except Exception as e:
        print("exception occurred:")
        print(e)
        return 1

if __name__ == '__main__':
    main()
