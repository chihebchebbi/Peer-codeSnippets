#!/usr/bin/env python 

import os
import sys
import time 

#Loading Bars and progress status


#using Percentages

"""for i in range(100):
    time.sleep(0.5)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()
"""

print ("Task in progress Here ...")	
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    	
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
    
