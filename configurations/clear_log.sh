#!/usr/bin/env bash

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

# Delete log files
echo -e "Deleting ${CYAN}log files${NC}..."
# sudo rm -rf /path/to/log/files/*
sudo rm /home/ge-wijayanto/python-sniffer/log_files/*

echo -e "${CYAN}Log files${NC} have been ${GREEN}deleted${NC}.\n"