# sshKeyManager
This script will check the information in the file against that available on the network, and update the information.

Instructions:
Give it a file called "NewKeys.txt" (sans quotes) in the keys folder, with the following format for each line:
[IP address],[full domain name],[optional: aliases separated by commas] [ssh format] [ssh key]

If no NewKeys file is available, it will use the most recent updated_keys file in the keys folder.

Directory structure:
* hosts: individual files named after each host, containing key type and key separated by a space
* keys: containing the main files:
  * NewKeys.txt new host list
  * updated_keys_[date] updated file list
* keys/oldKeyLists: containing prior keylists. 

errorlog is in top directory.

TODO:
* get aliases from teh interwebz pull nis
* extend non-verbose mode
* figure out paths from argvs in hostListMaker
