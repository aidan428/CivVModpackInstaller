"""Used to uninstall modpack"""
import shutil
import os
from options.installModpack import get_civ_dir
from colorama import Fore, Back, Style


def uninstall_modpack():
    civ_path = str(get_civ_dir()) + "\Assets\DLC\MP_MODSPACK"
    exists = os.path.exists(civ_path)

    try:
        if exists == True:
            try:
                shutil.rmtree(civ_path)
                print(Fore.YELLOW + "Modpack has been uninstalled!")
            except Exception as e:
                print(Fore.RED + "Unable to uninstall!" + Style.RESET_ALL)
        elif exists == False:
            print(Fore.YELLOW + "Modpack is not installed!" + Style.RESET_ALL)
    except Exception as e:
        print(e)