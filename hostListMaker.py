# Nazim Karaca made this, with Will Weber's help, for University of Delaware in 2016.
#!/usr/bin/env python2

from sys import argv
import os
import socket
hostfilename = argv[1] #alternative filenaming mechanism, better because passed by prior script

NewHostList = open(hostfilename, "a")
path = "./hosts/keys/"

# append all the correct codes 
hostlist = os.listdir(path)
for file in hostlist:
    try:
        ip = socket.gethostbyname(file)
        content = open(path+file,"r").read()
        content.replace(" ",",")
        NewHostList.write(ip+","+file+","+content+"\n")
    except socket.gaierror:
        # host-not-available actions:
        print file+" not found on the network, ignoring it." # should we skip this step? It might be as fast this way.
        # keep old host info
        # should this be implemented? best to ask? Maybe  a cutoff date?

# print "Here's your file %r:" % NewHostList
# print NewHostList.read()

NewHostList.close()
