#!/bin/bash

#This script is written for a lab on a cloud guru. It's goal is to back up a user's /work directory to a new directory, /work_backup. This script will also create a log file and log all actions to a log file stored in the user's home directory. In order to ensure that the script will work even if the backup directory doesn't exist or is destroyed, it will also create the backup directory.

#create backup directory and log this
echo "Creating backup directory" >> /home/cloud_user/backup_logs
mkdir /home/cloud_user/work_backup

#copy files and log this
echo "Copying files" >> /home/cloud_user/backup_logs
cp -v /home/cloud_user/work/* /home/cloud_user/work_backup/ >> /home/cloud_user/backup_logs
echo "Finished copying files" >> /home/cloud_user/backup_logs

