# Nazim Karaca made this, with Will Weber's help, for University of Delaware in 2016.
#!/usr/bin/env python2

from sys import argv
import os
import socket
import re
hostfilename = argv[1] #alternative filenaming mechanism, better because passed by prior script

NewHostList = open(hostfilename, "a")
hostspath = "./hosts/"
keyspath = "./keys/"

# errorlog = open("errorlog", "a")

# append all the correct codes 
hostlist = os.listdir(hostspath)
for file in hostlist:
    try:
        ip = socket.gethostbyname(file)
        content = open(hostspath+file,"r").read()
        content.replace(" ",",")
        NewHostList.write(ip+","+file+","+content+"\n")
        print "Updated: "+file
    except socket.gaierror:
        # keep old host info
        OldHostList = open(argv[2], "r")
        for line in OldHostList:
            if file in line:
                print file+" not found on the network, keeping old info in updated list."
                NewHostList.write(line)
        OldHostList.close()
        
# if argv[2] != "": print "Here's your file %r:" % NewHostList

NewHostList.close()
