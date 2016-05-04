# sshKeyManager

directory structure:
* hosts: individual files named after each host, containing key type and key separated by a space
* keys: containing the main files:
  * sample.txt new host list
  * updated_keys_[date] most recent updated file list
  * errorlog 
* keys/oldKeyLists: containing prior keylists. 

TODO:
non-verbose mode (dump most printing to errorlog)
figure out paths from argvs in hostListMaker
give updateHosts a way to take in a new host list
