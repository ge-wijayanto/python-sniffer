## Python Script to Scan for Available Network Connection

import subprocess

def scan():
    cmd = "nmcli -m multiline -f ALL dev wifi"

    # Check for available network
    devices = subprocess.call(cmd, shell=True)

    # Display the information
    print(devices)

if __name__ == '__main__' :
    scan()