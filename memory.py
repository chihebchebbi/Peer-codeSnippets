#!/usr/bin/env python 

import os,sys
from termcolor  import colored


bannerMemory = """


 -------------------------------------------------------
 |                      Memory Analysis                |
 -------------------------------------------------------
"""


print bannerMemory
print colored("[OK]","green"),"Memory Malware Analysis"
print colored("[OK]","green"),"Collecting Memory Dumps ..."
print "Memory Linux Malware Analysis"


#configure  the PATH and the Profile 
#VolaPATH = "volatility --info " 
#os.system(VolaPATH + "| grep linux")
#os.system(VolaPATH + "| grep windows")

print ("[ OK ] pslist")
print ("[ OK ] pstree")
print ("[ OK ] pidhashtable")
print ("[ OK ] psaux")
print ("[ OK ] psenv")
print ("[ OK ] Threads")
print ("[ OK ] pslist")
print ("[ OK ] pstree")
print ("[ OK ] pidhashtable")
print ("[ OK ] psenv")
print ("[ OK ] netstat")
print ("[ OK ] Ifconfig")
print ("[ OK ] TList_raw")
print ("[ OK ] Library List")
print ("[ OK ] Kernel Opened Files")

#os.system(VolaPATH + "pslist")
#os.system(VolaPATH + "pstree")
#os.system(VolaPATH + "pidhashtable")
#os.system(VolaPATH + "psaux")
#os.system(VolaPATH + "psenv")
#os.system(VolaPATH + "threads")
#os.system(VolaPATH + "netstat")
#os.system(VolaPATH + "ifconfig")
#os.system(VolaPATH + "list_raw")
#os.system(VolaPATH + "library_list")
#os.system(VolaPATH + "kernel_opened_files")


