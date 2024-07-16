"""Ping several servers and ensure an internet connection"""
from pythonping import ping
from colorama import init
from colorama import Fore, Back, Style
import sys

domains = ['spaldotechoperations.co.uk', 'api.spaldotechoperations.co.uk', 'mods.spaldotechoperations.co.uk', 'repo.spaldotechoperations.co.uk']


def ping_google():
    response_list = ping('google.com', timeout=4)    
    status = response_list.rtt_avg_ms
    return status

def ping_spaldotechoperations():
    response_list = ping(domains, )

def print_google_results():
    init()
    print("Beginning internet connectivity test...")
    status = ping_google()

    if status == 4000.0:
        print(Fore.RED + "Connection timeout! Please check internet connectivity!")
        sys.exit(1)
    else:
        print(Fore.GREEN + "Internet connection established. Average ping time to Google is " + str(status) + "ms" + Style.RESET_ALL)
        print("\n")

def print_spaldotechops_results():
    init()
    for url in domains:
        response = ping(url)
        if response.rtt_avg_ms == 4000.0:
            print(Fore.YELLOW + url + Fore.RED + "        OFFLINE")       
        else:
            print(Fore.YELLOW + url + Fore.GREEN + "        ONLINE")


    print(Fore.LIGHTCYAN_EX + "\nPlease check service status above. If there are any offline, please contact the system administrator.\n")
    

