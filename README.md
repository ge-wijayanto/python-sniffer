# Python Packet Sniffer
### Author: Gregorius Evangelist W. / 140810190040


This repository contains a Packet Sniffer program and documentation developed using the Python language and intended for use on Raspberry Pi. Submitted by the author as a research project for the Final Project in Computer Science at Universitas Padjadjaran.


## Description
A Packet Sniffer is a tool (either software or hardware) that can be used to capture network packets in a process known as packet capture. The use of a Packet Sniffer typically reveals packet headers and various other information that can be used to understand network behavior or configuration. This information is valuable for tasks such as network monitoring, security testing, and actual security attacks.

In this research, the Packet Sniffer is developed using the Python language, specifically for socket programming domain, with the following utilities:
* Available Network Scanning
* Network Connection/Profile Configuration - Establishment
* Main Packet Sniffing Function
* Packet Sniffing Result Parsing
* Packet Capture Dumping
* Sending Log Files to a Remote Server


## Documentation Section
To simplify repository navigations, use these buttons:
<p>
    <a style="margin-right: 15px;" href="https://github.com/ge-wijayanto/python-sniffer#program-design">
        <img src="https://images-ext-2.discordapp.net/external/_vwOEpICdyxopjRrRwKZbtIV4Rln0b1WWrlYzh83GaI/%3Ft%3DDESIGN%26f%3DUbuntu-Bold%26ts%3D18%26tc%3Dfff%26hp%3D10%26vp%3D12%26w%3D105%26h%3D40%26c%3D12%26bgt%3Dunicolored%26bgc%3D45d27e%26be%3D1/https/dabuttonfactory.com/button.png">
    </a>
    <a style="margin-right: 15px;" href="https://github.com/ge-wijayanto/python-sniffer#installation">
        <img src="https://images-ext-2.discordapp.net/external/SRGXHDYU2YmkjYACWIaLxjR_-FZq--oykeLT4YdygCc/%3Ft%3DINSTALL%26f%3DUbuntu-Bold%26ts%3D18%26tc%3Dfff%26hp%3D10%26vp%3D12%26w%3D105%26h%3D40%26c%3D12%26bgt%3Dunicolored%26bgc%3D45d27e%26be%3D1/https/dabuttonfactory.com/button.png">
    </a>
    <a style="margin-right: 15px;" href="https://github.com/ge-wijayanto/python-sniffer#usage-guide">
        <img src="https://images-ext-1.discordapp.net/external/fBTMixxR9UPwNZY_I7rdseNmVAXBwQxCrWf3v5QjFug/%3Ft%3DUSAGE%26f%3DUbuntu-Bold%26ts%3D18%26tc%3Dfff%26hp%3D10%26vp%3D12%26w%3D105%26h%3D40%26c%3D12%26bgt%3Dunicolored%26bgc%3D45d27e%26be%3D1/https/dabuttonfactory.com/button.png">
    </a>
    <a style="margin-right: 15px;" href="https://github.com/ge-wijayanto/python-sniffer#demo">
        <img src="https://images-ext-1.discordapp.net/external/chF6kcQLINux4nRyKM3zfcMXTVnJALJGFp6-vGnZ3XE/%3Ft%3DDEMO%26f%3DUbuntu-Bold%26ts%3D18%26tc%3Dfff%26hp%3D10%26vp%3D12%26w%3D105%26h%3D40%26c%3D12%26bgt%3Dunicolored%26bgc%3D45d27e%26be%3D1/https/dabuttonfactory.com/button.png">
    </a>
</p>


## Program Design
### Flowchart
![Flowchart](img/FlowchartEnglish.png)
### Topology
![Topologi](img/Topologi.png)


## Installation
```sh
git clone https://github.com/ge-wijayanto/python-sniffer
cd python-sniffer
chmod +x install.sh
./install.sh
```


## Usage Guide
```
# Start Main Console
sudo python3 py-sniff.py

usage: runprog.py [-h] [-nS] [-c] [-s]

py-sniff - A Python Packet Sniffer

optional arguments:
  -h, --help      show this help message and exit
  -nS, --netscan  Scan for available networks
  -c, --connect   Connect to a network
  -s, --sniff     Start packet sniffing function

########### USAGE EXAMPLE ###########

# Step 1: Run Main Console Program in Console
$ sudo python3 py-sniff.py

# Step 2: Input the Desired Commands in Main Console Prompt
## Network Scan
py-sniff > -nS  # or --netscan

## Connect to a Network
py-sniff > -c   # or --connect

## Start Packet Sniffing
py-sniff > -s   # or --sniff
```


## Demo
### Installation Process
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/5980ebff-6088-4192-ad8a-8fd9d46e166f
### Main Console
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/06fcf40e-34d8-42e1-af0f-3e224f85e784
### Available Network Scanning & Establishing Connection
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/f4c351cb-ceb7-42f5-a0a9-b932daaa124c
### Sniff All Network Traffic
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/2cf10d6b-a90e-4cb4-a3bf-3f0feef0c4c7
### Sniff Specific Network Port
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/4d79d958-c975-45a2-9c9e-cea213fb5940
### Send Log, Clear Log, & Add Cron Job Scripts
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/51476c67-5f0c-4669-920b-b942305b202a
### Check Log Existence in Remote Server
https://github.com/ge-wijayanto/python-sniffer/assets/67153733/5e041cd4-6226-40ad-b5a0-f7798656e44f
