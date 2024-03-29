import socket
import binascii
from colorama import Style, Fore, Back
from bitstring import BitArray

def getEthernetHeader(eth):
    print('---------------------------------------------------------------------')
    
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}Ethernet Header:{Style.RESET_ALL}')
    print(f'     - Src. MAC\t\t: {Fore.GREEN}{binascii.hexlify(eth[1]).decode("utf-8").upper()}{Style.RESET_ALL}')
    print(f'     - Dest. MAC\t: {Fore.GREEN}{binascii.hexlify(eth[0]).decode("utf-8").upper()}{Style.RESET_ALL}')
    
def getIPHeader(ip):
    split_version_IHL = BitArray(hex(ip[0]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}IP Header:{Style.RESET_ALL}')
    print(f'     - IP Version\t: {Fore.GREEN}{split_version_IHL.bin[:4]} ({int(split_version_IHL.bin[:4], 2)}){Style.RESET_ALL}')
    print(f'     - Protocol\t\t: {Fore.GREEN}{ip[6]}{Style.RESET_ALL}')
    print(f'     - Src. IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[8])}{Style.RESET_ALL}')
    print(f'     - Dest. IP\t\t: {Fore.GREEN}{socket.inet_ntoa(ip[9])}{Style.RESET_ALL}')
    
def getTCPHeader(tcp):
    split_HL_flags = BitArray(hex(tcp[4]))
    split_flags = BitArray(hex(tcp[5]))
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}TCP Header:{Style.RESET_ALL}')
    print(f'     - Src. Port\t: {Fore.GREEN}{tcp[0]}{Style.RESET_ALL}')
    print(f'     - Dest. Port\t: {Fore.GREEN}{tcp[1]}{Style.RESET_ALL}')
    print(f'     - Flags\t\t: {Fore.GREEN}{split_HL_flags[4:] + split_flags[0:]}{Style.RESET_ALL}')
    print('         |---> URG: {3}{0}{4}, ACK: {3}{1}{4}, PSH: {3}{2}{4}'
          .format(
              split_flags.bin[2], 
              split_flags.bin[3], 
              split_flags.bin[4], 
              Fore.GREEN, 
              Style.RESET_ALL
              )
          )
    print('         |---> RST: {3}{0}{4}, SYN: {3}{1}{4}, FIN: {3}{2}{4}'
          .format(
              split_flags.bin[5], 
              split_flags.bin[6], 
              split_flags.bin[7], 
              Fore.GREEN, 
              Style.RESET_ALL
              )
          )
        
def getUDPHeader(udp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}UDP Header:{Style.RESET_ALL}')
    print(f'     - Src. Port\t: {Fore.GREEN}{udp[0]}{Style.RESET_ALL}')
    print(f'     - Dest. Port\t: {Fore.GREEN}{udp[1]}{Style.RESET_ALL}')

def getICMPHeader(icmp):
    print(f'[{Fore.CYAN}!{Style.RESET_ALL}] {Fore.CYAN}ICMP Header:{Style.RESET_ALL}')
    print(f'     - Type\t\t: {Fore.GREEN}{icmp[0]}{Style.RESET_ALL}')
    print(f'     - Code\t\t: {Fore.GREEN}{icmp[1]}{Style.RESET_ALL}')
    print(f'     - Identifier\t: {Fore.GREEN}{icmp[3]}{Style.RESET_ALL}')