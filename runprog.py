import argparse

import core_functions.network_scan as network_scan
import core_functions.connect as connect
import core_functions.sniff_all as sniff_all
import core_functions.sniff_port as sniff_port

cmd_parser = argparse.ArgumentParser(description='py-sniff - A Python Packet Sniffer', formatter_class=argparse.RawTextHelpFormatter)

cmd_parser.add_argument('-nS', '--netscan', action='store_true', help='Scan for available networks')
cmd_parser.add_argument('-c', '--connect', action='store_true', help='Connect to a network')
cmd_parser.add_argument('-sA', '--sniff_all', action='store_true', help='Start packet sniffing on network (All Packets)')
cmd_parser.add_argument('-sP', '--sniff_port', action='store_true', help='Start packet sniffing on a specific application port')
cmd_parser.add_argument('-s', '--sniff', action='store_true', help='Start packet sniffing function')

args = vars(cmd_parser.parse_args())

if args['netscan']:
    network_scan.main()
    exit(0)
elif args['connect']:
    connect.main()
    exit(0)
elif args['sniff_all']:
    sniff_all.main()
    exit(0)
elif args['sniff_port']:
    sniff_port.main()
    exit(0)
elif args['sniff']:
    sniff_func.main()
    exit(0)