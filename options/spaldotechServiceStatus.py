from multiprocessing.spawn import prepare
import os
from colorama import init
from colorama import Fore, Back, Style
from urllib.request import urlopen
from time import sleep
import shutil

def check_env():
    try:
        shutil.rmtree("temp")
    except Exception as e:
        e = e

def prepare_env():
    try:
        os.mkdir("temp")
    except Exception as e:
        print("Temporary folder already created")

def root_check():
    domain = "www.spaldotech.co.uk"
    url = "https://www.spaldotech.co.uk/robots.txt"
    save_as = "temp/RootRobot.txt"
    
    try:
        with urlopen(url) as file:
            content = file.read().decode()
        with open(save_as, "w") as download:
            download.write(content)
        statusStr = domain + "            "+ Fore.GREEN + "ONLINE" + Style.RESET_ALL
    except Exception as e:
        statusStr = domain + "            "+ Fore.RED + "OFFLINE" + Style.RESET_ALL
    print(statusStr)



def api_check():
    domain = "api.spaldotech.co.uk"
    url = "https://api.spaldotech.co.uk/robots.txt"
    save_as = "temp/APIRobot.txt"

    try:
        with urlopen(url) as file:
            content = file.read().decode()
        with open(save_as, "w") as download:
            download.write(content)
        statusStr = domain + "            "+ Fore.GREEN + "ONLINE" + Style.RESET_ALL
        statusInt = 1
    except Exception as e:
        statusStr = domain + "            "+ Fore.RED + "OFFLINE" + Style.RESET_ALL
        statusInt = 0
        print(e)
    print(statusStr)
    return statusInt


def vision_check():
    domain = "vision.spaldotech.co.uk"
    url = "https://vision.spaldotech.co.uk/.robots.txt"
    save_as = "temp/VisionRobot.txt"

    try:
        with urlopen(url) as file:
            content = file.read().decode()
        with open(save_as, "w") as download:
            download.write(content)
        statusStr = domain + "         "+ Fore.GREEN + "ONLINE" + Style.RESET_ALL
    except Exception as e:
        statusStr = domain + "         "+ Fore.RED + "OFFLINE" + Style.RESET_ALL
    print(statusStr)

def repo_check():
    domain = "repo.spaldotech.co.uk"
    url = "https://repo.spaldotech.co.uk/ModpackMenuResources/version.txt"
    save_as = "temp/RepoRobot.txt"

    try:
        with urlopen(url) as file:
            content = file.read().decode()
        with open(save_as, "w") as download:
            download.write(content)
        statusStr = domain + "           "+ Fore.GREEN + "ONLINE" + Style.RESET_ALL
    except Exception as e:
        statusStr = domain + "           "+ Fore.RED + "OFFLINE" + Style.RESET_ALL
    print(statusStr)


def check_status():
    print(Fore.YELLOW + "Checking Spaldotech Service Status..." + Style.RESET_ALL)
    sleep(3)
    check_env()
    prepare_env()
    sleep(1)
    root_check()
    sleep(3)
    api_check()
    sleep(3)
    repo_check()
    sleep(3)
    vision_check()
    sleep(3)
    print("\n" + Fore.YELLOW + "Please check service status above. If there are any offline, please contact the system administrator." + Style.RESET_ALL)
    print("\n")
    check_env()





