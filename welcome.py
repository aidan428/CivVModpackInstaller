import os
from colorama import Fore, Back, Style
from playsound import playsound
import click
import menu



art = ''' ______     ______   ______     __         _____     ______     ______   ______     ______     __  __    
/\  ___\   /\  == \ /\  __ \   /\ \       /\  __-.  /\  __ \   /\__  _\ /\  ___\   /\  ___\   /\ \_\ \   
\ \___  \  \ \  _-/ \ \  __ \  \ \ \____  \ \ \/\ \ \ \ \/\ \  \/_/\ \/ \ \  __\   \ \ \____  \ \  __ \  
 \/\_____\  \ \_\    \ \_\ \_\  \ \_____\  \ \____-  \ \_____\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/     \/_/\/_/   \/_____/   \/____/   \/_____/     \/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                                                                         '''

art2 = '''███████╗██████╗  █████╗ ██╗     ██████╗  ██████╗ ████████╗███████╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██║     ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
███████╗██████╔╝███████║██║     ██║  ██║██║   ██║   ██║   █████╗  ██║     ███████║
╚════██║██╔═══╝ ██╔══██║██║     ██║  ██║██║   ██║   ██║   ██╔══╝  ██║     ██╔══██║
███████║██║     ██║  ██║███████╗██████╔╝╚██████╔╝   ██║   ███████╗╚██████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
'''

art3 = '''███████ ██████   █████  ██      ██████   ██████  ████████ ███████  ██████ ██   ██ 
██      ██   ██ ██   ██ ██      ██   ██ ██    ██    ██    ██      ██      ██   ██ 
███████ ██████  ███████ ██      ██   ██ ██    ██    ██    █████   ██      ███████ 
     ██ ██      ██   ██ ██      ██   ██ ██    ██    ██    ██      ██      ██   ██ 
███████ ██      ██   ██ ███████ ██████   ██████     ██    ███████  ██████ ██   ██                                                                                
''' 




def print_art() :
  print(art2)
  print(Back.GREEN + "Welcome " + get_user_name() + " to the Civilisation V Modpack Installer " + Style.RESET_ALL)

def get_user_name():
  username = os.getlogin().capitalize()
  return username

def clear_screen():
  click.clear()

def back_to_menu():
  print(Fore.YELLOW + "Simply choose an option below by typing the menu number and pressing enter." + Style.RESET_ALL)
  print("\n")

def intro_music():
  playsound('assets/welcome.mp3')

def generate_welcome():
  clear_screen()
  print_art()
  intro_music()
