import os
import subprocess
import binascii
import socket

def logger(eth, ip, protocol, filename, counter):
    if os.path.exists('log_files'):
        log = open("log_files/log_" + filename + '.txt', 'a')
    else:
        subprocess.call('mkdir log_files', shell=True)
        log = open("log_files/log_" + filename + '.txt', 'a')
        
    log.write('---------------------------------------------------------------------\n')
    log.write('Packet Number ' + str(counter) +'\n\n')

    log.write(f'[!] Ethernet Header:\n')
    log.write(f'     - Destination MAC\t\t: {binascii.hexlify(eth[0]).decode("utf-8").upper()}\n')
    log.write(f'     - Source MAC\t\t: {binascii.hexlify(eth[1]).decode("utf-8").upper()}\n')
    log.write(f'     - Type/Length\t\t: {binascii.hexlify(eth[2]).decode("utf-8")}\n\n')

    log.write(f'[!] IP Header:\n')
    split_version_IHL = BitArray(hex(ip[0]))
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
        split_HL_flags = BitArray(hex(protocol[4]))
        split_flags = BitArray(hex(protocol[5]))
        log.write(f'[!] TCP Header:\n')
        log.write(f'     - Source Port\t\t: {protocol[0]}\n')
        log.write(f'     - Destination Port\t\t: {protocol[1]}\n')
        log.write(f'     - Sequence Number\t\t: {protocol[2]}\n')
        log.write(f'     - Acknowledgement Number\t: {protocol[3]}\n')
        log.write(f'     - Header Length\t\t: {split_HL_flags.bin[:4]} ({int(split_HL_flags.bin[:4], 2)*4} bytes ({int(split_HL_flags.bin[:4], 2)})\n')
        log.write(f'     - Flags\t\t\t: {protocol[5]}\n')
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
        log.write(f'     - Window Size\t\t: {protocol[6]}\n')
        log.write(f'     - Checksum\t\t\t: {protocol[7]}\n')
        log.write(f'     - Urgent Pointer\t\t: {protocol[8]}\n')
    elif ip[6] == 17:
        log.write(f'[!] UDP Header:\n')
        log.write(f'     - Source Port\t\t: {protocol[0]}\n')
        log.write(f'     - Destination Port\t\t: {protocol[1]}\n')
        log.write(f'     - Length\t\t\t: {protocol[2]}\n')
        log.write(f'     - Checksum\t\t\t: {protocol[3]}\n')
    elif ip[6] == 1:
        log.write(f'[!] ICMP Header:\n')
        log.write(f'     - Type\t\t\t: {protocol[0]}\n')
        log.write(f'     - Code\t\t\t: {protocol[1]}\n')
        log.write(f'     - Checksum\t\t\t: {protocol[2]}\n')
        log.write(f'     - Identifier\t\t: {protocol[3]}\n')
        log.write(f'     - Sequence Number\t\t: {protocol[4]}\n')
    else:
        log.write(f'[!] Not using TCP/UDP/ICMP Protocol\n')
    
    log.close()