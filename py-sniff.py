import subprocess
import sys
import os
from banner import banner
from runprog import *
from colorama import Style, Fore, Back

history_list = []
cmd = ''

# Command Input Handler
def inputHandler():
    global history_list
    global cmd

    while True:
        try:
            cmd = input(f'\npy-sniff > ')
            if cmd != 'history':
                history_list.append(cmd.strip())
            elif cmd.strip() == 'clear':
                subprocess.call('clear', shell=True)
            
            if cmd.strip() == 'history':
                if len(history_list) > 0:
                    for i in range(0, len(history_list)):
                        print(f'{i} ' + history_list[i])
                else:
                    print('History is Empty')
            elif cmd == 'exit' or cmd == 'quit':
                sys.exit('\nQuitting Program.\n')
            else:
                subprocess.call(f'python3 runprog.py {cmd}', shell=True)
        except KeyboardInterrupt:
            sys.exit('\nKeyboardInterrupt, Terminating Program.\n')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        banner()
    
    if not 'SUDO_UID' in os.environ.keys():
        print(f'\n[{Fore.RED}!{Style.RESET_ALL}] Attention\t: {Fore.RED}Run this script with Root Privileges get the expected behavior!{Style.RESET_ALL}')

    inputHandler()
