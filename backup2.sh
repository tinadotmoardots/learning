#!/bin/bash

#This script is written for a lab on a cloud guru. It's goal is to back up a user's /work directory to a new directory, /work_backup. This script will also create a log file and log all actions to a log file stored in the user's home directory. In order to ensure that the script will work even if the backup directory doesn't exist or is destroyed, it will also create the backup directory.

#version 2 of this script defines variables and uses them to make locations universal for all users
LOGFILE="/home/$USER/log_file"
BACKUP_LOC="/usr/bin/*"
BACKUP_TARGET="/home/$USER/backup-variables"

#create backup directory and log this
echo "Creating backup directory" && mkdir $BACKUP_TARGET 2> /dev/null || echo "Directory already exists."

#copy files and log this
echo "Copying files" && cp -v $BACKUP_LOC $BACKUP_TARGET > $LOGFILE 2&1

grep -i denied $LOGFILE | tail -n 2

exit 127
