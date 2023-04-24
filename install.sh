#!/usr/bin/env bash

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

echo -e "\n${RED}NOTICE!!${NC}"
echo -e "If your Raspberry Pi doesn't support ${CYAN}Monitor Mode${NC}, please run ${GREEN}patch.sh${NC} first!!"
echo -e "Press ${GREEN}ENTER${NC} to continue..."
read -p ""

echo -e "\nInitiating ${CYAN}Py-Sniff (Python Sniffer)${NC} installation process...\n"

yes | sudo apt update && sudo apt upgrade

# Install the latest version of Python 3
yes | sudo apt install python3

# Install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# Install dependencies
yes | sudo apt install net-tools
yes | sudo apt install network-manager

# Install modules
yes | sudo pip install colorama
yes | sudo pip install bitstring
yes | sudo pip install sockets
yes | sudo pip install argparse

# Create Log Files Directory
sudo mkdir log_files/
sudo chmod 700 log_files/

# Change permissions to configuration directory
sudo chmod 700 configurations/
sudo chmod 700 configurations/log_server.sh
sudo chmod 700 configurations/cron_setup.sh
# /<path to file>/python-sniffer/configurations/cron_setup.sh
/home/ge-wijayanto/python-sniffer/configurations/cron_setup.sh

echo -e "The installation process is ${GREEN}complete${NC}."