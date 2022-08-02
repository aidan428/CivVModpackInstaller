"""Script used to download and install modpack"""
from time import sleep
from tkinter import E
import winapps
import os
import requests
import shutil
from zipfile import ZipFile
from colorama import Fore, Back, Style


def check_env():
    try:
        os.remove("MP_MODSPACK.zip")
        print(Fore.YELLOW + "Purged old installer files" + Style.RESET_ALL)
    except Exception as e:
        e = e
    

def get_civ_dir():
    print(Fore.GREEN + "Attempting to automatically locate your Civilisation V install location...")

    for item in winapps.search_installed("Sid Meier's Civilization V"):
        locationPath = item.install_location
        locationStr = str(locationPath)
        exists = os.path.exists(locationStr + "\CivilizationV.exe")
        try:
            if exists == False:
                continue
            elif exists == True:
                print(Fore.GREEN + "Your Civilisation V install directory has been located.")
                return locationPath
                break
        except Exception as e:
            print(Fore.RED + "Unable to locate Civilisation V. Please contact Mr Spalding." + Style.RESET_ALL)

def download_modpack():
    url = r"https://repo.spaldotech.co.uk/Civ%20V/Modded%20Server%20Resources/MP_MODSPACK.zip"
    save_as = "Download/MP_MODPACK.zip"
    try:
        req = requests.get(url)
        filename = url.split('/')[-1]

        with open(filename, 'wb') as output_file:
            output_file.write(req.content)
            print(Fore.GREEN + "Download completed successfully!")
    except Exception as e:
        e = e
        print(Fore.RED + "Failed to download Modpack. Please check your internet connection!")

def install_modpack():
    civ_path = str(get_civ_dir()) + "\Assets\DLC"
    check_env()
    print(Fore.YELLOW + "Attempting to download the modpack archive...")
    download_modpack()

    if os.path.exists(civ_path + "\MP_MODSPACK") == True:
        print(Fore.YELLOW + "The modpack has already been installed. Please uninstall it first if you tend to reinstall it!" + Style.RESET_ALL)
        os._exit(1)
    try:
        with ZipFile("MP_MODSPACK.zip", 'r') as zip:
            zip.extractall(civ_path)
            print(Fore.GREEN + "Install Complete!" + Style.RESET_ALL)
            print("\n")
    except Exception as e:
        print(e)
        print(Fore.RED + "Failed to install. Please contact Mr Spalding and show him the above error trace." + Style.RESET_ALL)

def cleanup():
    os.remove("MP_MODSPACK.zip")
    


        
        



