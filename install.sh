#!/usr/bin/env bash

sudo apt update && sudo apt upgrade

# Install the latest version of Python 3
sudo apt install python3

# Install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# Install dependencies
sudo apt install net-tools
sudo apt install network-manager

# Install modules
sudo pip install colorama
sudo pip install bitstring
sudo pip install sockets
sudo pip install argparse

# Create Log Files Directory
sudo mkdir log_files/
chmod 777 log_files/