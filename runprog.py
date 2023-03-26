import subprocess
import os
import argparse
from colorama import Style, Fore, Back

import core_functions.network_scan as network_scan
import core_functions.connect as connect
import core_functions.sniff_func as sniff_func

cmd_parser = argparse.ArgumentParser(description='py-sniff - A Python Packet Sniffer', formatter_class=argparse.RawTextHelpFormatter)

cmd_parser.add_argument('-s', '--scan', action='store_true', help='Scan for available networks')
cmd_parser.add_argument('-c', '--connect', action='store_true', help='Connect to a network')
cmd_parser.add_argument('-S', '--sniff', action='store_true', help='Start packet sniffing on network')

args = vars(cmd_parser.parse_args())

if args['scan']:
    network_scan.main()
    exit(0)
elif args['connect']:
    connect.main()
    exit(0)
elif args['sniff']:
    sniff_func.main()
    exit(0)