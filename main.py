#!/usr/bin/env python
# Developed by Chiheb Chebbi 2017


"""
@author:       Chiheb Chebbi
@license:      GNU General Public License 2.0
@contact:      chiheb.chebbi@tek-up.de
@Description:  Analyses Linux Malware by performing static, dynamic and memory analysis
"""

import sys,os
import hashlib 
import time
import requests
import json
#import yara
import socket
from termcolor  import colored
from optparse import OptionParser

banner = """
 
                        Linux Malware Analysis Sandbox 1.0-beta
                             Developed by Chiheb Chebbi

"""

print colored(banner,"blue")
#print ("Usage:")
#print ("Command [options] <file> [arguments]")


#Option verification
if len(sys.argv) <=1:
	print colored("Please Enter a valid option to start the Malware Analysis Or Type --help ","red")
	sys.exit()


REMOTE_SERVER = "www.tek-up.de"
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return "Internet"
  except:
     pass
     return False
print is_connected()

parser = OptionParser('Usage: Command [Options] <file> [args]')

#parser.add_option("-h", "--help", action="store_true", dest="help", help = "Dispaly Help Message",  default=False)
parser.add_option("-d", "--dynamic", action="store_true", dest="dynamic", help="Dynamic Malware Analysis",  default=False)
parser.add_option("-s", "--static", action="store_true", dest="static", help = "Static Malware Analysis",  default=False)
parser.add_option("-v", "--version", action="store_true", dest="version", help="Display the version of this application",  default=False)
parser.add_option("-m", "--memory", action="store_true", dest="memory", help="Full Memory Forensics",  default=False)

(options, args) = parser.parse_args()

#help = options.help
static = options.static
dynamic = options.dynamic
memory = options.memory
version = options.version

#Post Request for Malware Scanning

params = {'apikey': '3a6eb41041b884c803b1a06ab24e6bb652a30e8634e1db0156693961f539d1cc'}
files = {'file': ('elf', open('elf', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
#print(json_response["permalink"])
#print(json_response["scan_id"])

#Retrieve Report - Get Request 

params = {'apikey': '3a6eb41041b884c803b1a06ab24e6bb652a30e8634e1db0156693961f539d1cc', 'resource': '7657fcb7d772448a6d8504e4b20168b8'}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  Malware Analysis Sandbox requests"
  }
response1 = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
json_response1 = response1.json()





#if help:
#	print("Display Help Message")

if static:
	print colored("[OK]","green"),"Static Malware Analysis"
	print colored("[OK]","green"),"Starting Information Gathering about the File ..."
	print colored("[OK] File Information","yellow")
	os.system("file elf")
#MD5 Hash
	print colored("[OK] MD5 Hash","yellow")
	print(hashlib.md5(open('elf','rb').read()).hexdigest())

#fuzzy hash(ssdeep hash)
	print colored("[OK] Fuzzy Hash","yellow")
	os.system("ssdeep elf")

#Strings (Uncomment Later)
	#print colored("[OK]Strings","yellow")
	#os.system("strings elf")
#ELF Headers Information
	print colored("[OK] ELF Headers:","yellow")
	os.system("readelf -h  elf")
#Dependencies of the Malware sample
	print colored("[OK] Malware Dependencies:","yellow")
	os.system(" ldd  elf")

#Online Scanning
        print colored("[OK] Malware Scanning:","yellow")
# Scanning Result
	print colored("Number of Antivirus scanners: "+ str(json_response1["total"]),"blue")
        print colored("Scan Date: "+ str(json_response1["scan_date"]),"blue")	
	print colored("Scan ID: "+ str(json_response1["scan_id"]),"blue")
# Live Scanner Results	(Uncomment Later)
	#print colored("Live Scanners: "+ str(json_response1["scans"]),"blue")





elif dynamic:
	print("Dynamic Malware Analysis")

	print "[ OK ]cleaning Inetsim logs "
	#os.remove("/home/ghost/Desktop/MalwareSandbox/elf")

	print "[ OK ]starting inetsim"
	os.system("sudo inetsim")
	#starting capturing Network packets
	os.system("sudo tcpdump -qn")
	
elif memory:
	print("Full Memory Analysis")


elif version:
	print("Linux Malware analysis Sandbox Beta Version 0.1 - Developed by Chiheb Chebbi")
