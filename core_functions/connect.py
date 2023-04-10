import subprocess
import getpass
from colorama import Style, Fore, Back

# Create a New Network Profile
def createNewNetworkConn(name, SSID, key):
    # XML Configuration
    config = '''<?xml version=\"1.0\"?>
    <WLANProfile xmlns='http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <name>""" + SSID + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + key + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    '''

    cmd = 'nmcli dev wifi connect "' + SSID + '" password "' + key + '"'
    subprocess.call(cmd, shell=True)

# Connect to Network
def connectToNetwork(name, SSID):
    cmd = 'nmcli con up ' + SSID
    subprocess.call(cmd, shell=True)

def main():
    userInput = input(f'{Fore.GREEN}NEW NETWORK? (Y/N) : {Style.RESET_ALL}')
    
    if userInput == 'N' or userInput == 'n':
        print(f'\n{Fore.CYAN}Connecting to a Known Network...\n{Style.RESET_ALL}')
        netname = input(f'{Fore.GREEN}Network Name\t\t: {Style.RESET_ALL}')
        connectToNetwork(netname,netname)
        print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] Attention\t\t: {Fore.YELLOW}If network is not recognized, try connecting with correct credentials{Style.RESET_ALL}')
    elif userInput == 'Y' or userInput == 'y':
        print(f'\n{Fore.CYAN}Creating a New Network Profile...\n{Style.RESET_ALL}')
        netname = input(f'{Fore.GREEN}Network Name\t\t: {Style.RESET_ALL}')
        passkey = getpass.getpass(f'{Fore.GREEN}Password\t\t: {Style.RESET_ALL}')
        createNewNetworkConn(netname,netname,passkey)
        connectToNetwork(netname,netname)
        print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] Attention\t\t: {Fore.YELLOW}If network is not recognized, try connecting with correct credentials{Style.RESET_ALL}')
    else:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t: {Fore.RED}Invalid Input!{Style.RESET_ALL}')