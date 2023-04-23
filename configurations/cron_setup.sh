#!/usr/bin/env bash

# Format for the cron job

# * * * * * command to be executed
# - - - - -
# | | | | |
# | | | | -- Day (0 - 7) (Sunday=0 or 7)
# | | | ---- Month (1 - 12)
# | | ------ Day of month (1 - 31)
# | -------- Hour (0 - 23)
# ---------- Minutes (0 - 59)

#write out current crontab
crontab -l > setcron

#echo new cron into cron file
echo "*/2 * * * * /bin/sh /home/ge-wijayanto/nexmon/configurations/log_server.sh" >> setcron

#install new cron file
crontab setcron
rm setcron