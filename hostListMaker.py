#!/bin/bash 
LOGFILE=errorlog # change to /dev/null if unwanted
date +"%Y_%m_%d" >> $LOGFILE


# get hosts from internal file, and then ssh-keyscan each one of them
cat keys/sample.txt | while read line; do 
    hostName=`echo $line | awk -F' ' '{print $1}' | awk -F',' '{print $2}'` #will give all host names in the key file
    # echo "Checking $hostName"
    keyInfo=`ssh-keyscan $hostName 2>>$LOGFILE | awk -F' ' '{print $2,$3}'` #will grab all key types and public keys
    
    #check if hostname file already esists, if not, create it 
    [ -r "hosts/$hostName" ] || touch "hosts/$hostName"
    
    # compare hostName and keyInfo to existing file, create .changed if different.
    if [ "$(< hosts/$hostName)" != "$keyInfo" -a -n "$keyInfo" ] ; then # 0 if true
        # write changes to a new file
        echo -n "$keyInfo" > hosts/${hostName}.changed
        # maybe TODO log actions?
        
        echo $hostName is different from our info. | tee -a $LOGFILE
    else
        #overwrite old info to file
        echo "Keeping old key file for $hostName because no response from network."
        echo $line | awk -F',' '{print $NF}' | awk -F' ' '{print $2,$3}' > hosts/${hostName}
    fi
done

if [ \! -e hosts/*.changed ] ; then
    echo 'No changes detected, doc. List NOT updated.'
else
    echo 'Hey, YOU! Commit dem changes? [Y/N]'
    read answer
    if [ $answer =  'Y' -o $answer = 'y' ] ; then
        for filename in hosts/*.changed 
        do
            mv ${filename} ${filename%%.changed} # why does this look at t5120-hw-etc...?
        done
        
        #TODO log actions
        mv keys/updated_keys* keys/oldKeylists/ # move old key file
        oldlist=$(ls -dt keys/oldKeylists/* | head -1)
        newlist=keys/updated_keys_`date +"%Y_%m_%d"`
        touch $newlist

        # run python script to dump info into that file
        exec python hostListMaker.py $newlist $oldlist
    fi
fi
