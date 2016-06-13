# Nazim Karaca made this, with Will Weber's help, for University of Delaware in 2016.
#!/usr/bin/env python2

from sys import argv
import os
import socket
import re
hostfilename = argv[1] #alternative filenaming mechanism, better because passed by prior script

NewHostList = open(hostfilename, "w")
hostspath = "./hosts/"
keyspath = "./keys/"
verbose = True

if verbose == False:
    errorlog = open("errorlog", "a")
    
# append all the correct codes 
hostlist = os.listdir(hostspath)
for file in hostlist:
    try:
        
        # get network feedback
        ip = socket.gethostbyname(file)
        content = open(hostspath+file,"r").read()
        content.replace(" ",",")
        
        # get host info including aliases
        host = ""
        # pull nis or dns info here
        OldHostList = open(argv[2], "r")
        for line in OldHostList:
            if file in line:
                host = line[0:line.find(" ")]
        OldHostList.close()

        # write the info
        NewHostList.write(host+" "+content+"\n")
        if verbose: print "Updated: "+file
        else: errorlog.write("Updated: "+file+" in "+hostfilename)
        
    except socket.gaierror:
        # alert the bosses and then eliminate the rest of this when nis is properly coded
        
        # keep old host info
        OldHostList = open(argv[2], "r")
        for line in OldHostList:
            if file in line:
                NewHostList.write(line)
                if verbose: print file+" not found on the network, keeping old info in updated list."
                else: errorlog.write(file+" not found on the network, keeping old info in updated list.")
        
        OldHostList.close()
        
NewHostList.close()
if verbose == False:
    errorlog.close()
