#!/usr/bin/env bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
runfile=$parent_path/startup.sh

# Fix permissions for the runfile
chmod 755 $runfile

# Add the runfile to the crontab
! (crontab -l | grep -q "$runfile") && (crontab -l; echo "@reboot $runfile") | crontab -