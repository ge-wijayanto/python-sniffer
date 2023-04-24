#!/usr/bin/env bash

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
sudo chmod 777 configurations/log_server.sh
sudo chmod 777 configurations/cron_setup.sh
# /<path to file>/python-sniffer/configurations/cron_setup.sh
/home/ge-wijayanto/python-sniffer/configurations/cron_setup.sh