#!/usr/bin/env bash

# IMPORTANT: This script is intended to automate Monitor Mode Patching on the Raspberry Pi using Nexmon.

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

echo -e "\n${RED}IMPORTANT!!${NC}"
echo -e "This script is intended to automate ${CYAN}Monitor Mode Patching${NC} on Raspberry Pi using ${GREEN}Nexmon${NC}."
echo -e "${CYAN}MONITOR MODE${NC} is required to properly run ${GREEN}PACKET SNIFFING ACTIVITIES${NC}.\n"

echo -e "${YELLOW}WARNING:${NC}"
echo -e "1. Patching a firmware could potentially ${RED}DAMAGE YOUR HARDWARE${NC}, so please ${YELLOW}PROCEED WITH EXTRA CAUTION${NC}."
echo -e "2. This script is intended to be used on ${CYAN}Raspberry Pi${NC} running ${GREEN}Raspbian OS${NC}."
echo -e "3. As of the time being, ${CYAN}NEXMON${NC} only supports the following firmware version:"
echo -e "   - bcm43455c0 -> ${GREEN}7.45.154${NC}, ${GREEN}7.45.189${NC}, ${GREEN}7.45.206${NC}${NC}"
echo -e "   - bcm43430a1 -> ${GREEN}7.45.41.26${NC}, ${GREEN}7.45.41.46${NC}"
echo -e "   - bcm43436b0 -> ${GREEN}9.88.4.65${NC}"
echo -e "4. As of the time being, ${CYAN}NEXMON${NC} supports kernel versions: ${GREEN}4.4${NC}, ${GREEN}4.9${NC}, ${GREEN}4.14${NC}, ${GREEN}4.19${NC}, ${GREEN}5.4${NC}, ${GREEN}5.10${NC}, ${GREEN}5.15${NC}."
echo -e "5. ${YELLOW}BEFORE YOU CONTINUE${NC}, make sure to edit ${GREEN}THIS SCRIPT${NC} to match the following:"
echo -e "   - ${CYAN}Kernel Version${NC} -> use '${GREEN}uname -r${NC}' to check"
echo -e "   - ${CYAN}Firmware Version of WiFi Chipset${NC} -> use '${GREEN}ethtool -i <interface>${NC} (such as wlan0)' to check"
echo -e "   - ${CYAN}Username/Hostname${NC} -> for any part of the script targeting directories"
echo -e "   - ${CYAN}Directory Path Name${NC} -> for any part that needs to be adjusted to your directory path name\n"

echo -e "All credits goes to ${GREEN}seemoo-lab${NC} for creating ${CYAN}NEXMON${NC} Monitor Mode patch scripts."
echo -e "Nexmon's GitHub Repository: ${GREEN}https://github.com/seemoo-lab/nexmon${NC}\n\n"

echo -e "The script will now proceed to patch the firmware of your WiFi Chipset..."
echo -e "If you haven't edited this script as mentioned in ${YELLOW}WARNING POINT 5${NC}, please do so first."
echo -e "If you have, Press ${GREEN}ENTER${NC} to continue..."
read -p ""

# Exclude the following Firmware Packages from being updated
sudo apt-mark hold firmware-brcm80211
sudo apt-mark hold firmware-realtek
sudo apt-mark hold firmware-atheros
sudo apt-mark hold firmware-libertas

# Update the system
yes | sudo apt update && sudo apt upgrade

# Install dependencies
yes | sudo apt install raspberrypi-kernel-headers git libgmp3-dev gawk qpdf bison flex make autoconf libtool texinfo

# Clone the Nexmon repository
git clone https://github.com/seemoo-lab/nexmon.git

# Change directory to Nexmon
cd nexmon

# Use root privileges
sudo su

# Compile libisl.so.10
# cd /<path_to_dir>/nexmon/buildtools/isl-0.10
cd /home/ge-wijayanto/nexmon/buildtools/isl-0.10 
autoreconf -f -i
./configure
make
make install
ln -s /usr/local/lib/libisl.so /usr/lib/arm-linux-gnueabihf/libisl.so.10
stat /usr/lib/arm-linux-gnueabihf/libisl.so.10

# Compile libmpfr.so.4
# cd /<path_to_dir>/nexmon/buildtools/mpfr-3.1.4
cd /home/ge-wijayanto/nexmon/buildtools/mpfr-3.1.4
autoreconf -f -i
./configure
make
make install
ln -s /usr/local/lib/libmpfr.so /usr/lib/arm-linux-gnueabihf/libmpfr.so.4
stat /usr/lib/arm-linux-gnueabihf/libmpfr.so.4

# Install patches
# cd /<path_to_dir>/nexmon/
cd /home/ge-wijayanto/nexmon/
source setup_env.sh
make

# Patch the firmware
# cd /<path_to_dir>/nexmon/patches/<wifi_chipset_model>/<firmware_version>/nexmon/
cd /home/ge-wijayanto/nexmon/patches/bcm43455c0/7_45_206/nexmon/
make
make backup-firmware
make install-firmware

# Install Nexutil
# cd /<path_to_dir>/nexmon/utilities/nexutil/
cd /home/ge-wijayanto/nexmon/utilities/nexutil/
make
make install

# Disable power saving features (to prevent firmware from crashing)
# iw dev <interface> set power_save off
iw dev wlan0 set power_save off

# Load the patched firmware
modinfo brcmfmac
# mv /lib/modules/<kernel_version>/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko /lib/modules/<kernel_version>/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko.orig
mv /lib/modules/5.10.103-v7+/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko /lib/modules/5.10.103-v7+/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko.orig
# cp /<path_to_dir>/nexmon/patches/driver/brcmfmac_<kernel_version>-nexmon/brcmfmac.ko /lib/modules/<kernel_version>/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko
cp /home/ge-wijayanto/nexmon/patches/driver/brcmfmac_5.10.y-nexmon/brcmfmac.ko /lib/modules/5.10.103-v7+/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko
depmod -a

# Reboot the system
echo -e "The patching process is complete, The system will now reboot."
echo -e "After rebooting, you can check if the patch succeeded by checking if the '${CYAN}monitor${NC}' capability is listed." 
echo -e "Use the following command: ${GREEN}iw list${NC}"
echo -e "Press ${GREEN}ENTER${NC} to continue..."
read -p ""
sudo reboot