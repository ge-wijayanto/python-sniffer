import socket
import struct
import sys
import os
import subprocess
import time
import tracemalloc
from colorama import Style, Fore, Back
from bitstring import BitArray

import additional_functions.write_log as write_log
import additional_functions.stats_calculator as stats_calc
import additional_functions.console_logger as console_log

def sniffAll():
    try:
        raw = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
    except KeyboardInterrupt:
        print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
        sys.exit()
    except socket.error as err:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{err[1]}{Style.RESET_ALL}')
    else:
        counter = 1
        timestamp = time.strftime('%a, %d %b %Y %H:%M', time.localtime())
        filename = timestamp
        
        while True:
            try:
                start = time.time()
                memory = tracemalloc.start()
                captured_packet = raw.recvfrom(65565)
                
                eth_header = captured_packet[0][0:14]
                eth = struct.unpack('!6s6s2s', eth_header)

                ip_header = captured_packet[0][14:34]
                ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                if ip[6] == 6:
                    tcp_header = captured_packet[0][34:54]
                    tcp = struct.unpack('!HHLLBBHHH', tcp_header)
                    
                    data_content = captured_packet[0][54:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                elif ip[6] == 17:    
                    udp_header = captured_packet[0][34:42]
                    udp = struct.unpack('!HHHH', udp_header)
                    
                    data_content = captured_packet[0][42:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                elif ip[6] == 1:
                    icmp_header = captured_packet[0][34:42]
                    icmp = struct.unpack('!BBHHH', icmp_header)
                    
                    data_content = captured_packet[0][42:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                
                ## Print
                if ip[6] == 6:
                    console_log.getEthernetHeader(eth)
                    console_log.getIPHeader(ip)
                    console_log.getTCPHeader(tcp)
                    # console_log.getData(data)
                    write_log.logger(eth, ip, tcp, data, filename, counter)
                    
                    print(f'\nWriting to log file...\n{Fore.CYAN}Check Log for a More Detailed Captured Header Fields Information{Style.RESET_ALL}')
                    end = time.time()
                    stats_calc.calculateStats(start, end, memory, counter)
                    counter += 1
                elif ip[6] == 17:
                    console_log.getEthernetHeader(eth)
                    console_log.getIPHeader(ip)
                    console_log.getUDPHeader(udp)
                    # console_log.getData(data)
                    write_log.logger(eth, ip, udp, data, filename, counter)
                    
                    print(f'\nWriting to log file...\n{Fore.CYAN}Check Log for a More Detailed Captured Header Fields Information{Style.RESET_ALL}')
                    end = time.time()
                    stats_calc.calculateStats(start, end, memory, counter)
                    counter += 1
                elif ip[6] == 1:
                    console_log.getEthernetHeader(eth)
                    console_log.getIPHeader(ip)
                    console_log.getICMPHeader(icmp)
                    # console_log.getData(data)
                    write_log.logger(eth, ip, icmp, data, filename, counter)
                    
                    print(f'\nWriting to log file...\n{Fore.CYAN}Check Log for a More Detailed Captured Header Fields Information{Style.RESET_ALL}')
                    end = time.time()
                    stats_calc.calculateStats(start, end, memory, counter)
                    counter += 1
                else:
                    continue
            except KeyboardInterrupt:
                print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
                sys.exit()
            except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{e}{Style.RESET_ALL}')

def sniffPort(port):
    try:
        raw = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
    except KeyboardInterrupt:
        print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
        sys.exit()
    except socket.error as err:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{err[1]}{Style.RESET_ALL}')
    else:
        counter = 1
        timestamp = time.strftime('%a, %d %b %Y %H:%M', time.localtime())
        filename = timestamp
        
        while True:
            try:
                start = time.time()
                memory = tracemalloc.start()
                captured_packet = raw.recvfrom(65565)
                
                eth_header = captured_packet[0][0:14]
                eth = struct.unpack('!6s6s2s', eth_header)

                ip_header = captured_packet[0][14:34]
                ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                if ip[6] == 6:
                    tcp_header = captured_packet[0][34:54]
                    tcp = struct.unpack('!HHLLBBHHH', tcp_header)
                    
                    data_content = captured_packet[0][54:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                elif ip[6] == 17:    
                    udp_header = captured_packet[0][34:42]
                    udp = struct.unpack('!HHHH', udp_header)
                    
                    data_content = captured_packet[0][42:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                elif ip[6] == 1:
                    icmp_header = captured_packet[0][34:42]
                    icmp = struct.unpack('!BBHHH', icmp_header)
                    
                    data_content = captured_packet[0][42:]
                    data = struct.unpack('!%ds' % len(data_content), data_content)
                
                ## Print
                if ip[6] == 6 and (tcp[0] == int(port) or tcp[1] == int(port)):
                    console_log.getEthernetHeader(eth)
                    console_log.getIPHeader(ip)
                    console_log.getTCPHeader(tcp)
                    # console_log.getData(data)
                    write_log.logger(eth, ip, tcp, data, filename, counter)
                    
                    print(f'\nWriting to log file...\n{Fore.CYAN}Check Log for a More Detailed Captured Header Fields Information{Style.RESET_ALL}')
                    end = time.time()
                    stats_calc.calculateStats(start, end, memory, counter)
                    counter += 1
                elif ip[6] == 17 and (udp[0] == int(port) or udp[1] == int(port)):
                    console_log.getEthernetHeader(eth)
                    console_log.getIPHeader(ip)
                    console_log.getUDPHeader(udp)
                    # console_log.getData(data)
                    write_log.logger(eth, ip, udp, data, filename, counter)
                    
                    print(f'\nWriting to log file...\n{Fore.CYAN}Check Log for a More Detailed Captured Header Fields Information{Style.RESET_ALL}')
                    end = time.time()
                    stats_calc.calculateStats(start, end, memory, counter)
                    counter += 1
                else:
                    continue
            except KeyboardInterrupt:
                print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}KeyboardInterrupt, Terminating Program.\n{Style.RESET_ALL}')
                sys.exit()
            except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t\t: {Fore.RED}{e}{Style.RESET_ALL}')
    
def main():
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t: {Fore.RED}ROOT PRIVILEGES REQUIRED!{Style.RESET_ALL}')
        print(f'Quitting program...')
        sys.exit()
    else:
        option = input(f'{Fore.GREEN}USE FILTER BY PORT SCANNING OPTION? (Y/N) : {Style.RESET_ALL}')
        
        if option == 'N' or option == 'n':
            print(f'\n{Fore.CYAN}Starting Packet Sniffing Activity on ALL PORT...\n{Style.RESET_ALL}')
            print(f'[{Fore.YELLOW}!{Style.RESET_ALL}] Attention\t: {Fore.YELLOW}Use Keyboard Interrupt (CTRL + C) to End Activity{Style.RESET_ALL}\n')
            time.sleep(3)
            sniffAll()
            log.close()
        elif option == 'Y' or option == 'y':
            port = input(f'{Fore.GREEN}INPUT PORT FILTER : {Style.RESET_ALL}')
            print(f'\n{Fore.CYAN}Starting Packet Sniffing Activity on {Fore.GREEN}PORT {port}{Fore.CYAN}...\n{Style.RESET_ALL}')
            print(f'[{Fore.YELLOW}!{Style.RESET_ALL}] Attention\t: {Fore.YELLOW}Use Keyboard Interrupt (CTRL + C) to End Activity{Style.RESET_ALL}\n')
            time.sleep(3)
            sniffPort(port)
            log.close()
        else:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] ERROR\t: {Fore.RED}Invalid Input!{Style.RESET_ALL}')
    
    log.close()