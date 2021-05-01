##!/bin/bash

#You work for Universe Incorporated. One of your users — cloud_user — has an already existing backup script. There's been a request from two other users — adent and zbee — to have the same script made available. Modify /home/cloud_user/backup.sh to include using bash variables for the user directories and user names. Feel free to include variables for anything else you'd like.

#Once complete, copy the script to the other user directories, and ensure it runs and successfully backs up the required files.

MYLOG=$1

echo "Creating backup directory" >> /home/$USER/$MYLOG
mkdir /home/$USER/work_backup

echo "Copying Files" >> /home/$USER/$MYLOG
cp -v /home/$USER/work/* /home/$USER/work_backup/ >> /home/$USER/$MYLOG
echo "Finished Copying Files" >> /home/$USER/$MYLOG