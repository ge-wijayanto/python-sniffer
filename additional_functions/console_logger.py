import socket
import binascii
from colorama import Style, Fore, Back
from bitstring import BitArray

def getEthernetHeader(eth):
    print('---------------------------------------------------------------------')
    
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}Ethernet Header:{Style.RESET_ALL}')
    # print(f'     - Destination MAC\t\t: {Fore.GREEN}{binascii.hexlify(eth[0]).decode("utf-8").upper()}{Style.RESET_ALL}')
    # print(f'     - Source MAC\t\t: {Fore.GREEN}{binascii.hexlify(eth[1]).decode("utf-8").upper()}{Style.RESET_ALL}')
    # print(f'     - Type/Length\t\t: {Fore.GREEN}{binascii.hexlify(eth[2]).decode("utf-8")}{Style.RESET_ALL}')
    print(f'     Src. MAC : {Fore.GREEN}{src}{Style.RESET_ALL}, Dest. MAC : {Fore.GREEN}{dest}{Style.RESET_ALL}'.format(
        src=binascii.hexlify(eth[1]).decode("utf-8").upper(),
        dest=binascii.hexlify(eth[0]).decode("utf-8").upper()
        ))
    
def getIPHeader(ip):
    split_version_IHL = BitArray(hex(ip[0]))
    # split_flags_fragment = BitArray(hex(ip[4]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}IP Header:{Style.RESET_ALL}')
    # print(f'     - IP Version\t\t: {Fore.GREEN}{split_version_IHL.bin[:4]} ({int(split_version_IHL.bin[:4], 2)}){Style.RESET_ALL}')
    # print(f'     - IP Header Length (IHL)\t: {Fore.GREEN}{split_version_IHL.bin[4:]} ({int(split_version_IHL.bin[4:], 2)*4} bytes ({int(split_version_IHL.bin[4:], 2)})){Style.RESET_ALL}')
    # print(f'     - Type of Service (TOS)\t: {Fore.GREEN}{ip[1]}{Style.RESET_ALL}')
    # print(f'     - Total Length\t\t: {Fore.GREEN}{ip[2]}{Style.RESET_ALL}')
    # print(f'     - Identification\t\t: {Fore.GREEN}{ip[3]}{Style.RESET_ALL}')
    # print(f'     - Flags\t\t\t: {Fore.GREEN}{split_flags_fragment.bin[:3]} ({hex(int(split_flags_fragment.bin[:3], 2))}){Style.RESET_ALL}')
    # print(f'     - Fragment Offset\t\t: {Fore.GREEN}{split_flags_fragment.bin[3:]} ({int(split_flags_fragment.bin[3:], 2)}){Style.RESET_ALL}')
    # print(f'     - Time-to-Live (TTL)\t: {Fore.GREEN}{ip[5]}{Style.RESET_ALL}')
    # print(f'     - Protocol\t\t\t: {Fore.GREEN}{ip[6]}{Style.RESET_ALL}')
    # print(f'     - Header Checksum\t\t: {Fore.GREEN}{hex(ip[7])}{Style.RESET_ALL}')
    # print(f'     - Source IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[8])}{Style.RESET_ALL}')
    # print(f'     - Destination IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[9])}{Style.RESET_ALL}')
    print(f'     IP Version : {Fore.GREEN}{ver_bits} ({ver_dec}){Style.RESET_ALL}, Protocol : {Fore.GREEN}{proto}{Style.RESET_ALL}'.format(
        ver_bits=split_version_IHL.bin[:4], 
        ver_dec=int(split_version_IHL.bin[:4], 2), 
        proto=ip[6]
        ))
    print(f'     Src. IP : {Fore.GREEN}{src}{Style.RESET_ALL}, Dest. IP : {Fore.GREEN}{dest}{Style.RESET_ALL}'.format(
        src=socket.inet_ntoa(ip[8]),
        dest=socket.inet_ntoa(ip[9])
        ))
    
def getTCPHeader(tcp):
    # split_HL_flags = BitArray(hex(tcp[4]))
    split_flags = BitArray(hex(tcp[5]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}TCP Header:{Style.RESET_ALL}')
    # print(f'     - Source Port\t\t: {Fore.GREEN}{tcp[0]}{Style.RESET_ALL}')
    # print(f'     - Destination Port\t\t: {Fore.GREEN}{tcp[1]}{Style.RESET_ALL}')
    # print(f'     - Sequence Number\t\t: {Fore.GREEN}{tcp[2]}{Style.RESET_ALL}')
    # print(f'     - Acknowledgement Number\t: {Fore.GREEN}{tcp[3]}{Style.RESET_ALL}')
    # print(f'     - Header Length\t\t: {Fore.GREEN}{split_HL_flags.bin[:4]} ({int(split_HL_flags.bin[:4], 2)*4} bytes ({int(split_HL_flags.bin[:4], 2)})){Style.RESET_ALL}')
    # print(f'     - Flags\t\t\t: {Fore.GREEN}{split_HL_flags[4:] + split_flags[0:]}{Style.RESET_ALL}')
    # print(f'          - Reserved\t\t: {Fore.GREEN}{split_HL_flags.bin[4:7]}{Style.RESET_ALL}')
    # print(f'          - Accurate ECN\t: {Fore.GREEN}{split_HL_flags.bin[7]}{Style.RESET_ALL}')
    # print(f'          - Congestion Window\t: {Fore.GREEN}{split_flags.bin[0]}{Style.RESET_ALL}')
    # print(f'          - ECN-Echo\t\t: {Fore.GREEN}{split_flags.bin[1]}{Style.RESET_ALL}')
    # print(f'          - URG\t\t\t: {Fore.GREEN}{split_flags.bin[2]}{Style.RESET_ALL}')
    # print(f'          - ACK\t\t\t: {Fore.GREEN}{split_flags.bin[3]}{Style.RESET_ALL}')
    # print(f'          - PSH\t\t\t: {Fore.GREEN}{split_flags.bin[4]}{Style.RESET_ALL}')
    # print(f'          - RST\t\t\t: {Fore.GREEN}{split_flags.bin[5]}{Style.RESET_ALL}')
    # print(f'          - SYN\t\t\t: {Fore.GREEN}{split_flags.bin[6]}{Style.RESET_ALL}')
    # print(f'          - FIN\t\t\t: {Fore.GREEN}{split_flags.bin[7]}{Style.RESET_ALL}')
    # print(f'     - Window Size\t\t: {Fore.GREEN}{tcp[6]}{Style.RESET_ALL}')
    # print(f'     - Checksum\t\t\t: {Fore.GREEN}{hex(tcp[7])}{Style.RESET_ALL}')
    # print(f'     - Urgent Pointer\t\t: {Fore.GREEN}{tcp[8]}{Style.RESET_ALL}')
    print(f'     Src. Port : {Fore.GREEN}{src}{Style.RESET_ALL}, Dest. Port : {Fore.GREEN}{dest}{Style.RESET_ALL}'.format(
        src=tcp[0],
        dest=tcp[1]
    ))
    print(f'     Flags : {Fore.GREEN}{split_HL_flags[4:] + split_flags[0:]}{Style.RESET_ALL}')
    print(f'       URG : {Fore.GREEN}{urg}{Style.RESET_ALL}, ACK : {Fore.GREEN}{ack}{Style.RESET_ALL}, PSH : {Fore.GREEN}{psh}{Style.RESET_ALL}'
          .format(
              urg=split_flags.bin[2],
              ack=split_flags.bin[3],
              psh=split_flags.bin[4]
              )
          )
    print(f'       RST : {Fore.GREEN}{rst}{Style.RESET_ALL}, SYN : {Fore.GREEN}{syn}{Style.RESET_ALL}, FIN : {Fore.GREEN}{fin}{Style.RESET_ALL}'
          .format(
              rst=split_flags.bin[5],
              syn=split_flags.bin[6],
              fin=split_flags.bin[7]
              )
          )
        
def getUDPHeader(udp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}UDP Header:{Style.RESET_ALL}')
    # print(f'     - Source Port\t\t: {Fore.GREEN}{udp[0]}{Style.RESET_ALL}')
    # print(f'     - Destination Port\t\t: {Fore.GREEN}{udp[1]}{Style.RESET_ALL}')
    # print(f'     - Length\t\t\t: {Fore.GREEN}{udp[2]}{Style.RESET_ALL}')
    # print(f'     - Checksum\t\t\t: {Fore.GREEN}{hex(udp[3])}{Style.RESET_ALL}')
    print(f'     Src. Port : {Fore.GREEN}{src}{Style.RESET_ALL}, Dest. Port : {Fore.GREEN}{dest}{Style.RESET_ALL}'.format(
        src=udp[0],
        dest=udp[1]
    ))

def getICMPHeader(icmp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}ICMP Header:{Style.RESET_ALL}')
    # print(f'     - Type\t\t\t: {Fore.GREEN}{icmp[0]}{Style.RESET_ALL}')
    # print(f'     - Code\t\t\t: {Fore.GREEN}{icmp[1]}{Style.RESET_ALL}')
    # print(f'     - Checksum\t\t\t: {Fore.GREEN}{hex(icmp[2])}{Style.RESET_ALL}')
    # print(f'     - Identifier\t\t: {Fore.GREEN}{icmp[3]}{Style.RESET_ALL}')
    # print(f'     - Sequence Number\t\t: {Fore.GREEN}{icmp[4]}{Style.RESET_ALL}')
    print(f'     Type : {Fore.GREEN}{icmp_type}{Style.RESET_ALL}, Code : {Fore.GREEN}{code}{Style.RESET_ALL}'.format(
        icmp_type=icmp[0],
        code=icmp[1]  
    ))
    print(f'     Identifier\t\t: {Fore.GREEN}{icmp[3]}{Style.RESET_ALL}')

# def getData(data):
#     print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}Data:{Style.RESET_ALL}')
#     print(f'     - Data\t\t\t: {Fore.GREEN}{data}{Style.RESET_ALL}')