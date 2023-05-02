import time
import subprocess
from colorama import Style, Fore, Back

def graphics():
    print()
    print(f'{Fore.CYAN}    ____                _____         _  ____ ____{Style.RESET_ALL}')
    print(f'{Fore.CYAN}   / __ \ __  __       / ___/ ____   (_)/ __// __/{Style.RESET_ALL}')
    print(f'{Fore.CYAN}  / /_/ // / / /______ \__ \ / __ \ / // /_ / /_  {Style.RESET_ALL}')
    print(f'{Fore.CYAN} / ____// /_/ //_____/___/ // / / // // __// __/  {Style.RESET_ALL}')
    print(f'{Fore.CYAN}/_/     \__, /       /____//_/ /_//_//_/  /_/     {Style.RESET_ALL}')
    print(f'{Fore.CYAN}       /____/                                     {Style.RESET_ALL}')

def description():
    print(f'{Fore.MAGENTA}Author{Style.RESET_ALL}\t\t: Gregorius Evangelist W. / 140810190040')
    print(f'{Fore.MAGENTA}Repo{Style.RESET_ALL}\t\t: https://github.com/ge-wijayanto/python-sniffer')
    print(f'{Fore.CYAN}\nDescription{Style.RESET_ALL}\t:')
    print(f'Py-Sniff (Python Sniffer) is a tool that is intended to assist Network Administrator & Cybersecurity Professionals') 
    print(f'for network monitoring and security testing activities. This tool has a core function of running Packet Sniffing')
    print(f'tasks and parsing the Packet Capture results. Other than that, it\'s also capable of doing other functions like:')
    print(f'  - Network Scanning')
    print(f'  - Establishing Network Profile & Connection')
    print(f'  - Logging/Dumping to TXT File')
    print(f'  - Sending Log Files to a Remote Server')
    print(f'\n[{Fore.YELLOW}!{Style.RESET_ALL}] Note\t: {Fore.YELLOW}This program is intended to be used in Raspberry Pi, but might run on other systems{Style.RESET_ALL}')
    print(f'\nInput {Fore.GREEN}"--help"{Style.RESET_ALL} or {Fore.GREEN}"-h"{Style.RESET_ALL} {Fore.CYAN}(without the quotation mark){Style.RESET_ALL} to see the list of available commands.')
    print(f'Use {Fore.GREEN}"quit"{Style.RESET_ALL} to quit the program & {Fore.GREEN}"history"{Style.RESET_ALL} to see command history {Fore.CYAN}(without the quotation mark){Style.RESET_ALL}.')
    
def banner():
    subprocess.call('clear', shell=True)
    graphics()
    description()
    time.sleep(1.5)