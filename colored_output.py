from colorama import Fore, Style
from getpass import getpass

# These will be user definable via garrick.conf
info_color = Fore.GREEN + Style.BRIGHT
error_color = Fore.RED + Style.BRIGHT
instruction_color = Fore.MAGENTA + Style.BRIGHT
side_color = Fore.YELLOW + Style.BRIGHT
prompt_color = Fore.CYAN + Style.BRIGHT
getpass_color = Fore.YELLOW + Style.BRIGHT

def print_info(string):
    print(info_color + string + Style.RESET_ALL)

def print_error(string):
    print(error_color + string + Style.RESET_ALL)

def print_instruction(string):
    print(instruction_color + string + Style.RESET_ALL)

def print_side(string):
    print(side_color + string + Style.RESET_ALL)

def colored_prompt(prompt):
    user_input = input(prompt_color + prompt + Style.RESET_ALL)
    return user_input

def colored_getpass(prompt):
    getpass(getpass_color + prompt + Style.RESET_ALL)
