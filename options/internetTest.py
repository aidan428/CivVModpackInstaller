"""Ping Google's servers and ensure an internet connection is alive"""
from pythonping import ping
from colorama import init
from colorama import Fore, Back, Style
import sys

def ping_google():
    response_list = ping('google.com', timeout=4)    
    status = response_list.rtt_avg_ms
    return status

def print_results():
    init()
    print("Beginning internet connectivity test...")
    status = ping_google()

    if status == 4000.0:
        print(Fore.RED + "Connection timeout! Please check internet connectivity!")
        sys.exit(1)
    else:
        print(Fore.GREEN + "Internet connection established. Average ping time to Google is " + str(status) + "ms" + Style.RESET_ALL)
        print("\n")

