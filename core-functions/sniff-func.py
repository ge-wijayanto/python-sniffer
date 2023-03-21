import socket
import struct
import sys
import os
import subprocess
import time
import tracemalloc
import binascii
from colorama import Style, Fore, Back

def calculateStats(start, end, memory, captured):
    # Calculate Runtime
    print(f'\n{Fore.MAGENTA}Elapsed Time: {Style.RESET_ALL}{(end - start)*1000}{Style.RESET_ALL}ms')
    
    # Calculate Memory Usage
    print(f'{Fore.MAGENTA}Memory Usage: {Style.RESET_ALL}{tracemalloc.get_traced_memory()} bytes')
    tracemalloc.stop()
    
    # Calculate Packets Captured
    print(f'{Fore.MAGENTA}Total Packets Captured: {Style.RESET_ALL}{captured} bytes')

def sniffStart():
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}ROOT PRIVILEGES REQUIRED!{Style.RESET_ALL}')
        print(f'Quitting program...')
        sys.exit()
    try:
        raw = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
    except KeyboardInterrupt:
        print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
        sys.exit()
    except socket.error as err:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{err[1]}{Style.RESET_ALL}')
    else:
        while True:
            try:
                start = time.time()
                memory = tracemalloc.start()
                captured_packet = raw.recvfrom(65565)
                
                print('----------------------------------------------------')

                # Ethernet Header Capture
                eth_header = captured_packet[0][0:14]
                eth = struct.unpack('!6s6s2s', eth_header)
                print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}Ethernet Header:{Style.RESET_ALL}')
                print(f'     - Destination MAC\t: {Fore.GREEN}{binascii.hexlify(eth[0]).upper().decode("utf-8")}{Style.RESET_ALL}')
                print(f'     - Source MAC\t: {Fore.GREEN}{binascii.hexlify(eth[1]).upper().decode("utf-8")}{Style.RESET_ALL}')
                print(f'     - Type/Length\t: {Fore.GREEN}{binascii.hexlify(eth[2]).decode("utf-8")}{Style.RESET_ALL}')

                # IP Header Capture
                ip_header = captured_packet[0][14:34]
                ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
                print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}IP Header:{Style.RESET_ALL}')
                # print(f'     - IP Header Length (IHL)\t: {Fore.GREEN}{ip[0].decode("utf-8")}{Style.RESET_ALL}')
                # print(f'     - Type of Service (TOS)\t: {Fore.GREEN}{ip[1].decode("utf-8")}{Style.RESET_ALL}')
                # print(f'     - Total Length\t: {Fore.GREEN}{ip[2]}{Style.RESET_ALL}')
                # print(f'     - Identification\t: {Fore.GREEN}{ip[3]}{Style.RESET_ALL}')
                # print(f'     - Fragment Offset\t: {Fore.GREEN}{ip[4]}{Style.RESET_ALL}')
                # print(f'     - Time-to-Live (TTL)\t: {Fore.GREEN}{ip[5].decode("utf-8")}{Style.RESET_ALL}')
                # print(f'     - Protocol\t\t: {Fore.GREEN}{ip[6].decode("utf-8")}{Style.RESET_ALL}')
                # print(f'     - Header Checksum\t: {Fore.GREEN}{ip[7]}{Style.RESET_ALL}')
                print(f'     - Source IP \t: {Fore.GREEN}{socket.inet_ntoa(ip[8])}{Style.RESET_ALL}')
                print(f'     - Destination IP \t: {Fore.GREEN}{socket.inet_ntoa(ip[9])}{Style.RESET_ALL}')
                
                end = time.time()
                
                calculateStats(start, end, memory, counter)
                counter += 1
            except KeyboardInterrupt:
                log.close()
                print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
                sys.exit()
            except Exception as e:
                log.close()
                print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{e}{Style.RESET_ALL}')

if __name__ == '__main__':
    timestamp = time.strftime('%a, %d %b %Y %H:%M', time.localtime())
    
    if os.path.exists('log_files'):
        log = open("log_files/log_" + timestamp + '.txt', 'a')
    else:
        subprocess.call('mkdir log_files', shell=True)
        log = open("log_files/log_" + timestamp + '.txt', 'a')

    counter = 1
    sniffStart()
    
    log.close()