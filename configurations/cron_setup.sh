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

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

echo -e "\n${RED}NOTICE!!${NC}"
echo -e "Adding ${CYAN}Cron Job Entry${NC} to ${GREEN}Cron Tables (Crontab)${NC}..."

#write out current crontab
crontab -l > setcron

#echo new cron into cron file
sudo echo "*/2 * * * * /bin/sh /home/ge-wijayanto/python-sniffer/configurations/log_server.sh" >> setcron

#install new cron file
crontab setcron
sudo rm setcron