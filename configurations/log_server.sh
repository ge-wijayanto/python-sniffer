RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
CYAN='\033[0;96m'
NC='\033[0m' # No Color

echo -e "\n${RED}NOTICE!!${NC}"
echo -e "Sending ${CYAN}log files${NC} to ${GREEN}Log Server${NC}..."

# SCP command
# scp -i <SSH Private Key> -r /path/to/local/log/files <username>@<Server IP/FQDN>:/path/to/remote/log/files
yes | scp -i ssh.key -r /home/ge-wijayanto/python-sniffer/log_files/ ge-wijayanto@log-server.duckdns.org:/home/ge-wijayanto/

echo -e "${CYAN}Log files${NC} have been sent to ${GREEN}Log Server${NC}.\n"

# Delete log files
# echo -e "Deleting ${CYAN}log files${NC}..."
# sudo rm -rf /path/to/log/files/*
# sudo rm -rf /home/ge-wijayanto/python-sniffer/log_files/*