#!/usr/bin/env bash

# IMPORTANT: This script is intended to automate Monitor Mode Patching on the Raspberry Pi using Nexmon.

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${RED}IMPORTANT!!${NC}"
echo -e "This script is intended to automate ${BLUE}Monitor Mode Patching${NC} on Raspberry Pi using ${GREEN}Nexmon${NC}."
echo -e "${BLUE}MONITOR MODE${NC} is required to properly run${GREEN}PACKET SNIFFING ACTIVITIES${NC}.\n"

echo -e "${YELLOW}WARNING:${NC}"
echo -e "1. Patching a firmware could potentially ${RED}DAMAGE YOUR HARDWARE${NC}, so please ${YELLOW}PROCEED WITH EXTRA CAUTION${NC}."
echo -e "2. This script is intended to be used on ${BLUE}Raspberry Pi${NC} running ${GREEN}Raspbian OS${NC}."
echo -e "3. As of the time being, ${BLUE}NEXMON${NC} only supports the following firmware version:"
echo -e "   - bcm43455c0 -> ${GREEN}7.45.154${NC}, ${GREEN}7.45.189${NC}, ${GREEN}7.45.206${NC}"
echo -e "   - bcm43430a1 -> ${GREEN}7.45.41.26${NC}, ${GREEN}7.45.41.46${NC}"
echo -e "   - bcm43436b0 -> ${GREEN}9.88.4.65${NC}"
echo -e "4. As of the time being, ${BLUE}NEXMON${NC} supports the kernel version: ${GREEN}4.4${NC}, ${GREEN}4.9${NC}, ${GREEN}4.14${NC}, ${GREEN}4.19${NC}, ${GREEN}5.4${NC}, ${GREEN}5.10${NC}, ${GREEN}5.15${NC}\n"
echo -e "5. ${YELLOW}BEFORE YOU CONTINUE${NC}, make sure to edit ${GREEN}THIS SCRIPT${NC} to match the following:"
echo -e "   - ${BLUE}Kernel Version${NC} -> by using '{$GREEN}uname -r{$NC}'"
echo -e "   - ${BLUE}Firmware Version of WiFi Chipset${NC} -> by using '{$GREEN}ethtool -i <interface>{$NC} (such as wlan0)'\n"

echo -e "All credits goes to ${GREEN}seemoo-lab${NC} for creating ${BLUE}NEXMON${NC} Monitor Mode patch scripts."
echo -e "Nexmon's GitHub Repository: ${GREEN}https://github.com/seemoo-lab/nexmon${NC}\n\n"

echo -e "The script will now proceed to patch the firmware of your WiFi Chipset..."
echo -e "If you haven't edited this script as mentioned in ${YELLOW}WARNING POINT 5${NC}, please do so first."
read -p "If you have Press ${GREEN}ENTER${NC} to continue..."