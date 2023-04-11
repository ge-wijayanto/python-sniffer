import tracemalloc
from colorama import Style, Fore, Back

def calculateStats(start, end, memory, captured):
    # Calculate Runtime
    print(f'\n{Fore.MAGENTA}Elapsed Time: {Style.RESET_ALL}{(end - start)*1000}{Style.RESET_ALL}ms')
    
    # Calculate Memory Usage
    print(f'{Fore.MAGENTA}Memory Usage: {Style.RESET_ALL}{tracemalloc.get_traced_memory()} bytes')
    tracemalloc.stop()
    
    # Calculate Packets Captured
    print(f'{Fore.MAGENTA}Total Packets Captured: {Style.RESET_ALL}{captured} packets\n')