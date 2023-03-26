import subprocess
import platform
import getpass

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

    if platform.system() == "Linux":
        cmd = "nmcli dev wifi connect '" + SSID + "' password '" + key + "'"
    elif platform.system() == "Windows":
        cmd = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
    
    subprocess.call(cmd, shell=True)

    if platform.system() == "Windows":
        subprocess.call("del " + name + ".xml")

# Function to Connect to Specific Network
def connectToNetwork(name, SSID):
    if platform.system() == "Linux":
        cmd = "nmcli con up " + SSID
    elif platform.system() == "Windows":
        cmd = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
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