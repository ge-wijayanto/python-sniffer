import subprocess
import platform
import getpass

# Function to Scan for Available Network
def scanAvailableNetwork():
    if platform.system() == "Linux":
        cmd = "nmcli -m multiline dev wifi list"
        subprocess.call(cmd, shell=True)
    elif platform.system() == "Windows":
        cmd = "netsh wlan show networks"
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    scanAvailableNetwork()