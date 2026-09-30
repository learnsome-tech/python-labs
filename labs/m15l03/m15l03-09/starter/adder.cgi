#!/usr/bin/env python3

import cgi   # NEW

def main(): # NEW except for the call to processInput
    form = cgi.FieldStorage()      # standard cgi script lines to here!
    
    # use format of next two lines with YOUR names and default data
