#!/usr/bin/env python

import os,sys
from optparse import OptionParser
 
#Args number verification
if len(sys.argv) <=1:
	print("Please give some arguments or type help!")
	sys.exit()


parser = OptionParser('Usage: %prog [Options] <file> [args]')

parser.add_option("-t", "--timeout", dest="timeout", help="timeout in seconds", default="False")
parser.add_option("-s", "--static", action="store_true", dest="static", help = "Static Malware Analysis",  default=False)
parser.add_option("-d", "--dynamic", action="store_true", dest="dynamic", help="Dynamic Malware Analysis",  default=False)

(options, args) = parser.parse_args()

timeout = options.timeout
static = options.static
dynamic = options.dynamic

if static:
	print("This is a static Malware Analysis")

elif dynamic:
	print("This is a dynamic Malware Analysis")
