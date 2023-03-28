import subprocess
import getpass
from colorama import Style, Fore, Back

# Function to Create a New Network Profile/Configuration
def createNewNetworkConn(name, SSID, key):
    # XML Configuration
    config = """<?xml version=\"1.0\"?>
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
    """

    cmd = "nmcli dev wifi connect '" + SSID + "' password '" + key + "'"
    subprocess.call(cmd, shell=True)

# Function to Connect to Specific Network
def connectToNetwork(name, SSID):
    cmd = "nmcli con up " + SSID
    subprocess.call(cmd, shell=True)

def main():
    userInput = input("New Network (Y/N): ")
    
    if userInput == "N" or userInput == "n":
        netname = input("Network Name: ")
        connectToNetwork(netname,netname)
        print("If network is not recognized, try connecting with correct credentials")
    elif userInput == "Y" or userInput == "y":
        netname = input("Network Name: ")
        passkey = getpass.getpass("Password: ")
        createNewNetworkConn(netname,netname,passkey)
        connectToNetwork(netname,netname)
        print("If network is not recognized, try connecting with correct credentials")
    else:
        print(f"[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}Invalid Input!{Style.RESET_ALL}")