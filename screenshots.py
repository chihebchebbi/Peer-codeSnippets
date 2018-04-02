#!/usr/bin/env python 

import os
import sys
import pyscreenshot as ImageGrab


print ("taking Screenshots")

# Pip install pyscreenshot
#Take Screenshots for the sandbox and Save them
im = ImageGrab.grab() 
ImageGrab.grab_to_file('im1.png')

