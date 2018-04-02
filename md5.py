#!/usr/bin/env python 

import hashlib 

print(hashlib.md5(open('myfile.exe','rb').read()).hexdigest())






