from options.internetTest import print_google_results, print_spaldotechops_results
from options.installModpack import install_modpack
from options.uninstallModpack import uninstall_modpack
from colorama import Fore, Back, Style
from time import sleep
import welcome


menu_options = {
    1: "Check Spaldotech Service Status",
    2: "Install the Civilisation V modpack",
    3: "Uninstall the Civilisation V modpack",
    0: "Exit"
}

def print_menu():
    for key in menu_options.keys():
        print (Fore.CYAN, key, Style.RESET_ALL, "--", menu_options[key] )

def menu_handler():
    while(True):
        welcome.back_to_menu()
        print_menu()
        print("\n")
        option = ''
        try:
            option = int(input(Fore.YELLOW + 'Enter menu option: ' + Style.RESET_ALL))
        except:
            print(Fore.RED + 'Error detecting option. Did you enter a number?' + Style.RESET_ALL)
        #Check what choice was entered and act accordingly
        if option == 1:
            #print("\n")
            welcome.clear_screen()
            print_google_results()
            print_spaldotechops_results()
            
        elif option == 2:
            install_modpack()
        elif option == 3:
            uninstall_modpack()
            
        elif option == 0:
            print(Fore.GREEN + Style.BRIGHT + "Thank you for using this tool!" + Style.RESET_ALL)
            # playsound('assets/touche.mp3')
            quit()
        else:
            print(Fore.RED + 'Invalid option. Please enter a number between 0 and 3.' + Style.RESET_ALL)
            print("\n")