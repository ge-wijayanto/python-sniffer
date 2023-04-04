import socket
import struct
import sys
import os
import subprocess
import time
import tracemalloc
import binascii
from colorama import Style, Fore, Back
from bitstring import BitArray

def calculateStats(start, end, memory, captured):
    # Calculate Runtime
    print(f'\n{Fore.MAGENTA}Elapsed Time: {Style.RESET_ALL}{(end - start)*1000}{Style.RESET_ALL}ms')
    
    # Calculate Memory Usage
    print(f'{Fore.MAGENTA}Memory Usage: {Style.RESET_ALL}{tracemalloc.get_traced_memory()} bytes')
    tracemalloc.stop()
    
    # Calculate Packets Captured
    print(f'{Fore.MAGENTA}Total Packets Captured: {Style.RESET_ALL}{captured} packets\n')

def sniffStart(log):
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
        counter = 1
        
        while True:
            try:
                start = time.time()
                memory = tracemalloc.start()
                captured_packet = raw.recvfrom(65565)
                
                print('---------------------------------------------------------------------')

                # Ethernet Header Capture
                eth_header = captured_packet[0][0:14]
                eth = struct.unpack('!6s6s2s', eth_header)
                getEthernetHeader(eth)

                # IP Header Capture
                ip_header = captured_packet[0][14:34]
                ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
                getIPHeader(ip)
                
                ## Check IP Header Protocol Field (TCP/UDP/ICMP)
                if ip[6] == 6:
                    tcp_header = captured_packet[0][34:54]
                    tcp = struct.unpack('!HHLLBBHHH', tcp_header)
                    getTCPHeader(tcp)
                    logger(log, eth, ip, tcp)
                elif ip[6] == 17:
                    udp_header = captured_packet[0][34:42]
                    udp = struct.unpack('!HHHH', udp_header)
                    getUDPHeader(udp)
                    logger(log, eth, ip, udp)
                elif ip[6] == 1:
                    icmp_header = captured_packet[0][34:42]
                    icmp = struct.unpack('!BBHHH', icmp_header)
                    getICMPHeader(icmp)
                    logger(log, eth, ip, icmp)
                else:
                    print(f'[{Fore.YELLOW}!{Style.RESET_ALL}] NOTE\t\t: {Fore.YELLOW}Not using TCP/UDP/ICMP Protocol{Style.RESET_ALL}')
                    
                ## Logging
                print('\nWriting to log...\n')
                
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

def getEthernetHeader(eth):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}Ethernet Header:{Style.RESET_ALL}')
    print(f'     - Destination MAC\t\t: {Fore.GREEN}{binascii.hexlify(eth[0]).decode("utf-8").upper()}{Style.RESET_ALL}')
    print(f'     - Source MAC\t\t: {Fore.GREEN}{binascii.hexlify(eth[1]).decode("utf-8").upper()}{Style.RESET_ALL}')
    print(f'     - Type/Length\t\t: {Fore.GREEN}{binascii.hexlify(eth[2]).decode("utf-8")}{Style.RESET_ALL}')
    
def getIPHeader(ip):
    split_version_IHL = BitArray(hex(ip[0]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}IP Header:{Style.RESET_ALL}')
    print(f'     - IP Version\t\t: {Fore.GREEN}{split_version_IHL.bin[:4]} ({int(split_version_IHL.bin[:4], 2)}){Style.RESET_ALL}')
    print(f'     - IP Header Length (IHL)\t: {Fore.GREEN}{split_version_IHL.bin[4:]} ({int(split_version_IHL.bin[4:], 2)*4} bytes ({int(split_version_IHL.bin[4:], 2)})){Style.RESET_ALL}')
    print(f'     - Type of Service (TOS)\t: {Fore.GREEN}{ip[1]}{Style.RESET_ALL}')
    print(f'     - Total Length\t\t: {Fore.GREEN}{ip[2]}{Style.RESET_ALL}')
    print(f'     - Identification\t\t: {Fore.GREEN}{ip[3]}{Style.RESET_ALL}')
    print(f'     - Fragment Offset\t\t: {Fore.GREEN}{ip[4]}{Style.RESET_ALL}')
    print(f'     - Time-to-Live (TTL)\t: {Fore.GREEN}{ip[5]}{Style.RESET_ALL}')
    print(f'     - Protocol\t\t\t: {Fore.GREEN}{ip[6]}{Style.RESET_ALL}')
    print(f'     - Header Checksum\t\t: {Fore.GREEN}{ip[7]}{Style.RESET_ALL}')
    print(f'     - Source IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[8])}{Style.RESET_ALL}')
    print(f'     - Destination IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[9])}{Style.RESET_ALL}')

def getTCPHeader(tcp):
    split_HL_flags = BitArray(hex(tcp[4]))
    split_flags = BitArray(hex(tcp[5]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}TCP Header:{Style.RESET_ALL}')
    print(f'     - Source Port\t\t: {Fore.GREEN}{tcp[0]}{Style.RESET_ALL}')
    print(f'     - Destination Port\t\t: {Fore.GREEN}{tcp[1]}{Style.RESET_ALL}')
    print(f'     - Sequence Number\t\t: {Fore.GREEN}{tcp[2]}{Style.RESET_ALL}')
    print(f'     - Acknowledgement Number\t: {Fore.GREEN}{tcp[3]}{Style.RESET_ALL}')
    print(f'     - Header Length\t\t: {Fore.GREEN}{split_HL_flags.bin[:4]} ({int(split_HL_flags.bin[:4], 2)*4} bytes ({int(split_HL_flags.bin[:4], 2)}){Style.RESET_ALL}')
    print(f'     - Flags\t\t\t: {Fore.GREEN}{tcp[5]}{Style.RESET_ALL}')
    print(f'          - Reserved\t\t: {Fore.GREEN}{split_HL_flags.bin[4:7]}{Style.RESET_ALL}')
    print(f'          - Accurate ECN\t: {Fore.GREEN}{split_HL_flags.bin[7]}{Style.RESET_ALL}')
    print(f'          - Congestion Window\t: {Fore.GREEN}{split_flags.bin[0]}{Style.RESET_ALL}')
    print(f'          - ECN-Echo\t\t: {Fore.GREEN}{split_flags.bin[1]}{Style.RESET_ALL}')
    print(f'          - URG\t\t\t: {Fore.GREEN}{split_flags.bin[2]}{Style.RESET_ALL}')
    print(f'          - ACK\t\t\t: {Fore.GREEN}{split_flags.bin[3]}{Style.RESET_ALL}')
    print(f'          - PSH\t\t\t: {Fore.GREEN}{split_flags.bin[4]}{Style.RESET_ALL}')
    print(f'          - RST\t\t\t: {Fore.GREEN}{split_flags.bin[5]}{Style.RESET_ALL}')
    print(f'          - SYN\t\t\t: {Fore.GREEN}{split_flags.bin[6]}{Style.RESET_ALL}')
    print(f'          - FIN\t\t\t: {Fore.GREEN}{split_flags.bin[7]}{Style.RESET_ALL}')
    print(f'     - Window Size\t\t: {Fore.GREEN}{tcp[6]}{Style.RESET_ALL}')
    print(f'     - Checksum\t\t\t: {Fore.GREEN}{tcp[7]}{Style.RESET_ALL}')
    print(f'     - Urgent Pointer\t\t: {Fore.GREEN}{tcp[8]}{Style.RESET_ALL}')
                    
def getUDPHeader(udp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}UDP Header:{Style.RESET_ALL}')
    print(f'     - Source Port\t\t: {Fore.GREEN}{udp[0]}{Style.RESET_ALL}')
    print(f'     - Destination Port\t\t: {Fore.GREEN}{udp[1]}{Style.RESET_ALL}')
    print(f'     - Length\t\t\t: {Fore.GREEN}{udp[2]}{Style.RESET_ALL}')
    print(f'     - Checksum\t\t\t: {Fore.GREEN}{udp[3]}{Style.RESET_ALL}')
    
def getICMPHeader(icmp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}ICMP Header:{Style.RESET_ALL}')
    print(f'     - Type\t\t\t: {Fore.GREEN}{icmp[0]}{Style.RESET_ALL}')
    print(f'     - Code\t\t\t: {Fore.GREEN}{icmp[1]}{Style.RESET_ALL}')
    print(f'     - Checksum\t\t\t: {Fore.GREEN}{icmp[2]}{Style.RESET_ALL}')
    print(f'     - Identifier\t\t: {Fore.GREEN}{icmp[3]}{Style.RESET_ALL}')
    print(f'     - Sequence Number\t\t: {Fore.GREEN}{icmp[4]}{Style.RESET_ALL}')

def logger(log, eth, ip, transport):
    log.write('---------------------------------------------------------------------\n')
    log.write('Packet Number ' + str(counter) +'\n\n')

    log.write(f'[!] Ethernet Header:\n')
    log.write(f'     - Destination MAC\t\t: {binascii.hexlify(eth[0]).decode("utf-8").upper()}\n')
    log.write(f'     - Source MAC\t\t: {binascii.hexlify(eth[1]).decode("utf-8").upper()}\n')
    log.write(f'     - Type/Length\t\t: {binascii.hexlify(eth[2]).decode("utf-8")}\n\n')

    log.write(f'[!] IP Header:\n')
    log.write(f'     - IP Version\t\t: {split_version_IHL.bin[:4]} ({int(split_version_IHL.bin[:4], 2)})\n')
    log.write(f'     - IP Header Length (IHL)\t: {split_version_IHL.bin[4:]} ({int(split_version_IHL.bin[4:], 2)*4} bytes ({int(split_version_IHL.bin[4:], 2)}))\n')
    log.write(f'     - Type of Service (TOS)\t: {ip[1]}\n')
    log.write(f'     - Total Length\t\t: {ip[2]}\n')
    log.write(f'     - Identification\t\t: {ip[3]}\n')
    log.write(f'     - Fragment Offset\t\t: {ip[4]}\n')
    log.write(f'     - Time-to-Live (TTL)\t: {ip[5]}\n')
    log.write(f'     - Protocol\t\t\t: {ip[6]}\n')
    log.write(f'     - Header Checksum\t\t: {ip[7]}\n')
    log.write(f'     - Source IP\t\t: {socket.inet_ntoa(ip[8])}\n')
    log.write(f'     - Destination IP\t\t: {socket.inet_ntoa(ip[9])}\n\n')
    
    if ip[6] == 6:
        split_HL_flags = BitArray(hex(tcp[4]))
        split_flags = BitArray(hex(tcp[5]))
        log.write(f'[!] TCP Header:\n')
        log.write(f'     - Source Port\t\t: {tcp[0]}\n')
        log.write(f'     - Destination Port\t\t: {tcp[1]}\n')
        log.write(f'     - Sequence Number\t\t: {tcp[2]}\n')
        log.write(f'     - Acknowledgement Number\t: {tcp[3]}\n')
        log.write(f'     - Header Length\t\t: {split_HL_flags.bin[:4]} ({int(split_HL_flags.bin[:4], 2)*4} bytes ({int(split_HL_flags.bin[:4], 2)})\n')
        log.write(f'     - Flags\t\t\t: {tcp[5]}\n')
        log.write(f'          - Reserved\t\t: {split_HL_flags.bin[4:7]}\n')
        log.write(f'          - Accurate ECN\t: {split_HL_flags.bin[7]}\n')
        log.write(f'          - Congestion Window\t: {split_flags.bin[0]}\n')
        log.write(f'          - ECN-Echo\t\t: {split_flags.bin[1]}\n')
        log.write(f'          - URG\t\t\t: {split_flags.bin[2]}\n')
        log.write(f'          - ACK\t\t\t: {split_flags.bin[3]}\n')
        log.write(f'          - PSH\t\t\t: {split_flags.bin[4]}\n')
        log.write(f'          - RST\t\t\t: {split_flags.bin[5]}\n')
        log.write(f'          - SYN\t\t\t: {split_flags.bin[6]}\n')
        log.write(f'          - FIN\t\t\t: {split_flags.bin[7]}\n')
        log.write(f'     - Window Size\t\t: {tcp[6]}\n')
        log.write(f'     - Checksum\t\t\t: {tcp[7]}\n')
        log.write(f'     - Urgent Pointer\t\t: {tcp[8]}\n')
    elif ip[6] == 17:
        log.write(f'[!] UDP Header:\n')
        log.write(f'     - Source Port\t\t: {udp[0]}\n')
        log.write(f'     - Destination Port\t\t: {udp[1]}\n')
        log.write(f'     - Length\t\t\t: {udp[2]}\n')
        log.write(f'     - Checksum\t\t\t: {udp[3]}\n')
    elif ip[6] == 1:
        log.write(f'[!] ICMP Header:\n')
        log.write(f'     - Type\t\t\t: {icmp[0]}\n')
        log.write(f'     - Code\t\t\t: {icmp[1]}\n')
        log.write(f'     - Checksum\t\t\t: {icmp[2]}\n')
        log.write(f'     - Identifier\t\t: {icmp[3]}\n')
        log.write(f'     - Sequence Number\t\t: {icmp[4]}\n')
    else:
        log.write(f'[!] Not using TCP/UDP/ICMP Protocol\n')

def main():
    timestamp = time.strftime('%a, %d %b %Y %H:%M', time.localtime())
    
    if os.path.exists('log_files'):
        log = open("log_files/log_" + timestamp + '.txt', 'a')
    else:
        subprocess.call('mkdir log_files', shell=True)
        log = open("log_files/log_" + timestamp + '.txt', 'a')

    sniffStart(log)
