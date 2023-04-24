#!/usr/bin/env bash

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

echo -e "\n${RED}NOTICE!!${NC}"
echo -e "If your Raspberry Pi doesn't support ${CYAN}Monitor Mode${NC}, please run ${GREEN}patch.sh${NC} first!!"
echo -e "${CYAN}Default permission${NC} for required folders and files are set to ${RED}777${NC}."
echo -e "Edit the ${GREEN}install.sh${NC} file (or manually) to change the ${YELLOW}permission${NC} according to your needs"
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
sudo chmod 777 log_files/

# Change permissions to configuration directory
sudo chmod 777 configurations/
sudo chmod 777 configurations/log_handler.sh
sudo chmod 777 configurations/cron_setup.sh
# /<path to file>/python-sniffer/configurations/cron_setup.sh
/home/ge-wijayanto/python-sniffer/configurations/cron_setup.sh

echo -e "The installation process is ${GREEN}complete${NC}."