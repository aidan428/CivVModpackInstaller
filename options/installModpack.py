"""Script used to download and install modpack"""
from tqdm import tqdm
from time import sleep
from tkinter import E
from zipfile import ZipFile
from colorama import Fore, Back, Style
import requests
import cgi
import sys
import winapps
import os
import shutil

download_link = r"https://repo.spaldotech.co.uk/Civ/LEKMOD_v30.7.zip"
file_name = "LEKMOD_v30.7.zip"


def check_env():
    civ_path = str(get_civ_dir()) + "\Assets\DLC\LEKMOD"
    exists = os.path.exists(civ_path)

    try:
        if exists == True:
            try:
                print(Fore.YELLOW + "Modpack is already installed! Please uninstall before proceeding.")
                quit()
            except Exception as e:
                print(Fore.RED + "Unable to detect installation status" + Style.RESET_ALL)
        elif exists == False:
            print(Fore.YELLOW + "Modpack is not installed!" + Style.RESET_ALL)
    except Exception as e:
        print(e)
    

def get_civ_dir():
    #print(Fore.GREEN + "Attempting to automatically locate your Civilisation V install location..." + Style.RESET_ALL)

    for item in winapps.search_installed("Sid Meier's Civilization V"):
        locationPath = item.install_location
        locationStr = str(locationPath)
        exists = os.path.exists(locationStr + "\CivilizationV.exe")
        try:
            if exists == False:
                continue
            elif exists == True:
                print(Fore.GREEN + "Your Civilisation V install directory has been automatically located." + Style.RESET_ALL)
                return locationPath
                break
        except Exception as e:
            print(Fore.RED + "Unable to locate Civilisation V. Please contact Mr Spalding." + Style.RESET_ALL)
            quit()

def download_modpack():
    #url = r"https://repo.spaldotech.co.uk/Civ/LEKMOD_V28.zip"
    
    buffer_size = 1024
    response = requests.get(download_link, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    default_filename = download_link.split("/")[-1]
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition:
        # parse the header using cgi
        value, params = cgi.parse_header(content_disposition)
        # extract filename from content disposition
        filename = params.get("filename", default_filename)
    else:
        # if content dispotion is not available, just use default from URL
        filename = default_filename
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))



def install_modpack():
    civ_path = str(get_civ_dir()) + "\Assets\DLC"
    check_env()
    print(Fore.YELLOW + "Attempting to download the modpack archive..." + Style.RESET_ALL)
    download_modpack()

    if os.path.exists(civ_path + "\LEKMOD") == True:
        print(Fore.YELLOW + "The modpack has already been installed. Please uninstall it first if you tend to reinstall it!" + Style.RESET_ALL)
        quit()
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall(civ_path)
            print(Fore.GREEN + "Install Complete!" + Style.RESET_ALL)
            print("\n")
    except Exception as e:
        print(e)
        print(download_link)
        print(Fore.RED + "Failed to install. Please contact Mr Spalding and show him the above error trace." + Style.RESET_ALL)

    cleanup()

def cleanup():
    os.remove(file_name)
    


        
        



