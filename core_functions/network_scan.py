import subprocess
import platform
import getpass
from colorama import Style, Fore, Back

# Function to Scan for Available Network
def scanAvailableNetwork():
    if platform.system() == "Linux":
        cmd = "nmcli -m multiline dev wifi list"
        subprocess.call(cmd, shell=True)
    elif platform.system() == "Windows":
        cmd = "netsh wlan show networks"
        subprocess.call(cmd, shell=True)

def main():
    print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}If you are prompted to a new window, use this key for navigation: {Style.RESET_ALL}')
    print(f'    - {Fore.GREEN}ARROW KEY{Style.RESET_ALL} or {Fore.GREEN}ENTER{Style.RESET_ALL} to continue to another line')
    print(f'    - {Fore.GREEN}SPACEBAR{Style.RESET_ALL} to continue to another page')
    print(f'    - {Fore.GREEN}Q{Style.RESET_ALL} key to return to py-sniff\'s main menu')
    
    scanAvailableNetwork()